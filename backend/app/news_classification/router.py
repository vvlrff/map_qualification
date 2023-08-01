from operator import and_
from fastapi import APIRouter, Depends
from sqlalchemy import select, cast, TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta

from app.database import get_async_session
from app.data_collection.models import news, country




router = APIRouter(
    prefix="/classification",
    tags=["Classification"]
)


@router.get("/news_guardian")
async def get_news_guardian(session: AsyncSession = Depends(get_async_session)):

    query = select(news)
    result = await session.execute(query)

    data = result.fetchall()
    answer = []
    for i in data:
        answer.append({
            'id': i[0],
            'title': i[1],
            'href': i[2],
            'date': i[3],
        })

    return answer


@router.get("/news/{start_date}/{end_date}")
async def get_news_by_date(start_date: str, end_date: str, session: AsyncSession = Depends(get_async_session)):
    # Преобразование строки даты в объект datetime
    start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
    end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")

    end_date_obj = end_date_obj.replace(hour=23, minute=59, second=59)

    # Создание запроса на выборку данных по дате
    stmt = select(news).where(and_(news.c.date >= start_date_obj, news.c.date <= end_date_obj))
    
    # Выполнение запроса и получение результатов
    result = await session.execute(stmt)
    data = result.fetchall()

    answer = []
    for i in data:
        answer.append({
            'id': i[0],
            'title': i[1],
            'href': i[2],
            'date': i[3],
        })

    return answer




@router.get("/countries_coordinates")
async def get_countries_coordinates(session: AsyncSession = Depends(get_async_session)):

    query = select(country)
    result = await session.execute(query)

    data = result.fetchall()
    answer = []
    for i in data:
        answer.append({
            'id': i[0],
            'text': i[1],
            'country': i[2],
            'date': i[3],
        })

    return answer

@router.get("/countries_coordinates/{start_date}/{end_date}")
async def get_news_by_date(start_date: str, end_date: str, session: AsyncSession = Depends(get_async_session)):
    # Преобразование строки даты в объект datetime
    start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
    end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")

    end_date_obj = end_date_obj.replace(hour=23, minute=59, second=59)
    
    # Создание запроса на выборку данных по дате
    stmt = select(country).where(and_(country.c.date >= start_date_obj, country.c.date <= end_date_obj))
    
    # Выполнение запроса и получение результатов
    result = await session.execute(stmt)
    data = result.fetchall()

    answer = []
    for i in data:
        answer.append({
            'id': i[0],
            'title': i[1],
            'href': i[2],
            'date': i[3],
        })

    return answer