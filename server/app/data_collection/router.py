from datetime import datetime
# from asyncpg import UniqueViolationError
from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.data_collection.models import news
from app.data_collection.services import dangerous_news_guardian

router = APIRouter(
    prefix="/collection",
    tags=["Collection"]
)


@router.get("/collect_news")
async def collect_news_guardian(session: AsyncSession = Depends(get_async_session)):

    data = dangerous_news_guardian()

    for i in data:
        news_title = i["title"]
        news_href = i["href"]
        news_country = i["country"]
        news_city = i["city"]
        news_image = i["image"]
        news_date = datetime.today()

        query = select(news).where(news.c.title == news_title)
        existing_entry = await session.execute(query)
        existing_entry = existing_entry.fetchone()

        if existing_entry is None:
            stmt = insert(news).values(
                title=news_title,
                href=news_href,
                date=news_date,
                city=news_city,
                country=news_country,
                image=news_image
            )
            await session.execute(stmt)
            await session.commit()

    return {
        "status": status.HTTP_200_OK,
        "data": data
    }
