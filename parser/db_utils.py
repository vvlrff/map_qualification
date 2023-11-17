from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

MONGO_URI = "mongodb://root:examplepassword@mongo:27017/"
client = AsyncIOMotorClient(MONGO_URI)

db = client["telegram_scraper_db"]
news_collection = db["news"]


async def load_channels_to_db(news_list):
    for news in news_list:
        await news_collection.update_one(
            {"news_title": news},
            {"$setOnInsert": {"channel_name": news, "last_post_number": None}},
            upsert=True,
        )


async def save_post_to_db(channel_name, post_number, message_text):
    await posts_collection.update_one(
        {"channel_name": channel_name, "post_number": post_number},
        {"$set": {"message_text": message_text}},
        upsert=True,
    )
    await channels_collection.update_one(
        {"channel_name": channel_name},
        {"$set": {"last_post_number": post_number}},
    )


async def send_posts_to_service():
    posts = await posts_collection.find({}).to_list(None)
    # Здесь ваш код для отправки постов другому микросервису. Например:
    # async with aiohttp.ClientSession() as session:
    #     await session.post('http://your_service_url/', json=posts)

    # После отправки удаляем посты из коллекции
    await posts_collection.delete_many({})
