import asyncio
import logging
import timeit

import aio_pika
import aiohttp
from bs4 import BeautifulSoup
import typing
import os
from db_utils import channels_collection, save_post_to_db
from shared.rabbit import SummaryMessage


MIN_WORD_COUNT = 5

username = os.getenv('RABBIT_USER') or 'guest'
password = os.getenv('RABBIT_PASSWORD') or 'guest'
host = os.getenv('RABBIT_HOST')
port = os.getenv('RABBIT_PORT') or 5672
virtual_host = os.getenv('RABBIT_VH') or '%2F'
queue_name = os.getenv('RABBIT_PARSER_QUEUE') or 'parser'
url = f'amqp://{username}:{password}@{host}:{port}/{virtual_host}'


async def generate_posts(
    session: aiohttp.ClientSession,
    channel_name: str,
    after: int | None
) -> typing.AsyncGenerator[tuple[int, str], None]:
    base_url = f'/s/{channel_name}'

    while True:
        url = f'{base_url}?after={after}' if after else base_url

        try:
            post_divs = await fetch_post_divs(session, url)
        except Exception as e:
            logging.error(f'Failed to extract posts from {channel_name}, error: {e}')
            return

        if not post_divs:
            return

        for post in post_divs:
            post_number, message = extract_post_info(post)
            if not message:
                continue
            yield int(post_number), message

        if not after or post_number == after:
            return
        after = post_number


async def fetch_post_divs(session: aiohttp.ClientSession, url: str):
    async with session.get(url, ssl=False) as response:
        page_content = await response.text()

    soup = BeautifulSoup(page_content, 'html.parser')
    post_divs = soup.find_all('div', {"class": "tgme_widget_message_wrap"})

    if post_divs and post_divs[0].find('div', {'class': 'tme_no_messages_found'}):
        return None
    return post_divs


def extract_post_info(post):
    message_div = post.find('div', {"class": "js-message_text"})
    meta_div = post.find('a', {"class": "tgme_widget_message_date"})

    post_number = meta_div['href'].split('/')[-1]
    message_text = message_div.get_text(' ') if message_div else None

    return post_number, message_text


async def process_channel(
    callback,
    session: aiohttp.ClientSession,
    channel_name: str,
    rabbit_channel: aio_pika.RobustChannel,
    last_post_number: int | None = None,
):
    after = int(last_post_number) if last_post_number is not None else None
    async for number, text in generate_posts(session, channel_name, after):
        if not after:
            continue
        if number <= after:
            continue
        if len(text.split()) < MIN_WORD_COUNT:
            continue
        await save_post_to_db(channel_name, number, text)
        await callback(channel_name, number, text, rabbit_channel, queue_name)


async def process_channels_in_parallel(callback):
    start_time = timeit.default_timer()
    try:
        connection = await aio_pika.connect_robust(url)
        rabbit_channel = await connection.channel()
        await rabbit_channel.declare_queue(queue_name)
    except Exception as e:
        logging.error(f"Failed to connect to RabbitMQ. Error: {e}")
        return
    channels = await channels_collection.find({}).to_list(None)
    async with aiohttp.ClientSession(base_url='https://t.me/') as session:
        tasks = [
            asyncio.create_task(process_channel(
                callback,
                session,
                channel['channel_name'],
                rabbit_channel,
                channel.get('last_post_number')
            ))
            for channel in channels
        ]
        await asyncio.gather(*tasks)
    await connection.close()
    elapsed_time = timeit.default_timer() - start_time
    logging.warning(f'{len(channels)} channels processed in {elapsed_time}')


async def async_print_post_info(
    channel_name,
    post_number,
    message_text,
    rabbit_ch: aio_pika.robust_channel.RobustChannel,
    rabbit_q: str
):
    summary_message = SummaryMessage(channel_name, post_number, message_text)
    msg = aio_pika.Message(
        bytes(summary_message),
        delivery_mode=aio_pika.DeliveryMode.PERSISTENT
    )
    await rabbit_ch.default_exchange.publish(
        msg,
        rabbit_q
    )
    logging.warning(f'Channel: {channel_name}, Post Number: {post_number}, Message: {message_text}')


async def main():
    logging.error('service initialized')
    while True:
        logging.error('another cycle started')
        await process_channels_in_parallel(async_print_post_info)
        await asyncio.sleep(10)


if __name__ == '__main__':
    asyncio.run(main())
