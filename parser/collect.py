import asyncio
import logging
from db_utils import save_to_mongo
from services import dangerous_news_guardian, get_guardian_news_items


url = 'https://www.theguardian.com/world'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.3.799 Yowser/2.5 Safari/537.36'
}


async def main():
    logging.error('service initialized')

    while True:
        logging.error('another cycle started')

        try:
            pars_data = get_guardian_news_items(url, headers=headers)
            news = dangerous_news_guardian(pars_data)

            await save_to_mongo(news)
        except Exception as e:
            logging.error(f'Failed to save news to mongo, error: {e}')
        
        await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())
