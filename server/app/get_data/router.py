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
            'title': i[1],
            'href': i[2],
            'image': i[3],
            'country': i[4],
            'city': i[5],
            'date': i[6],
        })
    return answer

@router.get("/news_guardian/{news_id}")
async def get_news_guardian_by_id(news_id: int, session: AsyncSession = Depends(get_async_session)):

    stmt = select(news).where(news.c.id == news_id)

    result = await session.execute(stmt)
    data = result.fetchone()

    return data


@router.get("/news_guardian_start_date={start_date}_end_date={end_date}")
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
            'title': i[1],
            'href': i[2],
            'image': i[3],
            'country': i[4],
            'city': i[5],
            'date': i[6],
        })

    return answer


