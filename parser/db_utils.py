import logging
from motor.motor_asyncio import AsyncIOMotorClient
import pymongo.errors


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MONGO_URI = "mongodb://root:examplepassword@mongo:27017/"
client = AsyncIOMotorClient(MONGO_URI)

db = client["scraper_db"]
news_collection = db["news"]

news_collection.create_index("title_en", unique=True)

async def save_to_mongo(data):
        for news in data:
            try:
                await news_collection.insert_one(news)
                logger.info(f"News {news['title_en']} saved to MongoDB")
            except pymongo.errors.DuplicateKeyError:
                logger.warning(f"News {news['title_en']} already exists in the database")


# async def load_news_to_db(news_list):
#     for news in news_list:
#         await news_collection.update_one(
#             {"news_title": news},
#             {"$setOnInsert": {"channel_name": news, "last_post_number": None}},
#             upsert=True,
#         )


# async def send_news_to_service():
#     news = await news_collection.find({}).to_list(None)
#     # Здесь ваш код для отправки постов другому микросервису. Например:
#     # async with aiohttp.ClientSession() as session:
#     #     await session.post('http://your_service_url/', json=posts)

#     # После отправки удаляем посты из коллекции
#     await news_collection.delete_many({})


# async def save_news_to_db(channel_name, post_number, message_text):
#     await news_collection.update_one(
#         {"channel_name": channel_name, "post_number": post_number},
#         {"$set": {"message_text": message_text}},
#         upsert=True,
#     )
#     await news_collection.update_one(
#         {"channel_name": channel_name},
#         {"$set": {"last_post_number": post_number}},
#     )