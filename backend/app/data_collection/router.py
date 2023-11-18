from datetime import datetime
from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.elastic import elastic_client
from app.database import get_async_session
from app.data_collection.models import news
from app.data_collection.services import dangerous_news_guardian


router = APIRouter(
    prefix="/collection",
    tags=["Collection"]
)


@router.post("/collect_news")
async def collect_news_guardian(session: AsyncSession = Depends(get_async_session)):

    data = dangerous_news_guardian()

    for i in data:
        news_title_en = i["title_en"]
        news_title_ru = i["title_ru"]
        news_href = i["href"]
        news_country = i["country"]
        news_city = i["city"]
        news_image = i["image"]
        news_topical_keywords = i["topical_keywords"]
        news_date = datetime.today()

        query = select(news).where(news.c.title_en == news_title_en)
        existing_entry = await session.execute(query)
        existing_entry = existing_entry.fetchone()

        if existing_entry is None:
            stmt = insert(news).values(
                title_en=news_title_en,
                title_ru=news_title_ru,
                href=news_href,
                date=news_date,
                city=news_city,
                country=news_country,
                image=news_image,
                topical_keywords=news_topical_keywords
            )
            await session.execute(stmt)
            await session.commit()

            document = {
                'title_en': news_title_en,
                'title_ru': news_title_ru,
                'href': news_href,
                'country': news_country,
                'city': news_city,
                'image': news_image,
                'topical_keywords': news_topical_keywords,
                'date': datetime.today().isoformat()
            }
            await elastic_client.index(index='news', document=document)

    return {"status": status.HTTP_200_OK, "data": data}
