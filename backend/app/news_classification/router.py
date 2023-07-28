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

@router.get("/news/{date}")
async def get_news_by_date(date: str, session: AsyncSession = Depends(get_async_session)):
    # Преобразование строки даты в объект datetime
    date_obj = datetime.strptime(date, "%d-%m-%Y")
    
    # Вычисление начальной и конечной даты для запроса
    start_date = date_obj.replace(hour=0, minute=0, second=0)

    end_date = datetime.today()
    date_column = cast(news.c.date, TIMESTAMP)

    
    # Создание запроса на выборку данных по дате
    stmt = select(news).where(news.c.date.between(start_date, end_date))
    
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

@router.get("/countries_coordinates/{date}")
async def get_news_by_date(date: str, session: AsyncSession = Depends(get_async_session)):
    # Преобразование строки даты в объект datetime
    date_obj = datetime.strptime(date, "%d-%m-%Y")
    
    # Вычисление начальной и конечной даты для запроса
    start_date = date_obj.replace(hour=0, minute=0, second=0)
    end_date = start_date + timedelta(days=1)
    
    # Создание запроса на выборку данных по дате
    stmt = select(country).where(country.c.date.between(start_date, end_date))
    
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