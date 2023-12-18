from urllib.parse import urlunsplit

from motor.motor_asyncio import AsyncIOMotorClient

from shared import settings


def get_mongodb_uri(
        username=settings.MONGO_USERNAME,
        password=settings.MONGO_PASSWORD,
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
        protocol=settings.MONGO_PROTOCOL,
        uri_query=settings.MONGO_URI_QUERY
):
    return urlunsplit((protocol, f'{username}:{password}@{host}:{port}', str(), uri_query, str()))


client = AsyncIOMotorClient(get_mongodb_uri())
