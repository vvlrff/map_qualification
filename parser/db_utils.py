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

