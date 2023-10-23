from operator import and_
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from app.database import get_async_session
from app.data_collection.models import news


router = APIRouter(
    prefix="/get",
    tags=["Get"]
)


@router.get("/news_guardian")
async def get_all_news_guardian(session: AsyncSession = Depends(get_async_session)):

    query = select(news)
    result = await session.execute(query)

    data = result.fetchall()
    answer = []
    for i in data:
        answer.append({
            'id': i[0],
            'title_en': i[1],
            'title_ru': i[2],
            'href': i[3],
            'image': f"http://localhost:8000/photos/{i[4]}",
            'image_text_ru': i[6],
            'image_text_en': i[5],
            'country': i[7],
            'city': i[8],
            'date': i[9],
        })

    return answer


@router.get("/news_guardian/{news_id}")
async def get_news_guardian_by_id(news_id: int, session: AsyncSession = Depends(get_async_session)):

    stmt = select(news).where(news.c.id == news_id)

    result = await session.execute(stmt)
    data = result.fetchone()

    answer = {
        'id': data[0],
        'title_en': data[1],
        'title_ru': data[2],
        'href': data[3],
        'image': f"http://localhost:8000/photos/{data[4]}",
        'image_text_ru': data[6],
        'image_text_en': data[5],
        'country': data[7],
        'city': data[8],
        'date': data[9],
    }

    return answer


@router.get("/news_guardian_{start_date}_{end_date}")
async def get_news_guardian_by_dates(start_date: str, end_date: str, session: AsyncSession = Depends(get_async_session)):

    start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
    end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")

    end_date_obj = end_date_obj.replace(hour=23, minute=59, second=59)

    stmt = select(news).where(
        and_(news.c.date >= start_date_obj, news.c.date <= end_date_obj))
    result = await session.execute(stmt)
    data = result.fetchall()

    answer = []
    for i in data:

        answer.append({
            'id': i[0],
            'title_en': i[1],
            'title_ru': i[2],
            'href': i[3],
            'image': f"http://localhost:8000/photos/{i[4]}",
            'image_text_ru': i[6],
            'image_text_en': i[5],
            'country': i[7],
            'city': i[8],
            'date': i[9],
        })

    return answer
