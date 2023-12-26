from fastapi import APIRouter, Depends
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from operator import and_
from datetime import datetime
from backend.app.data.models import news
from backend.app.database import get_async_session


router = APIRouter(
    prefix="/data",
    tags=["Data"]
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
            'country': i[5],
            'city': i[6],
            'date': i[7],
        })

    return {"result": answer}


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
        'country': data[5],
        'city': data[6],
        'date': data[7],
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
            'country': i[5],
            'city': i[6],
            'date': i[7],
        })

    return {"result": answer}


@router.delete("/news/{news_id}")
async def delete_news_by_id(news_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(news).where(news.c.id == news_id)

    await session.execute(stmt)
    await session.commit()

    return {"message": f"Новость {news_id} удалена успешно"}


@router.delete("/news")
async def delete_all_news(session: AsyncSession = Depends(get_async_session)):
    stmt = delete(news)

    await session.execute(stmt)
    await session.commit()

    return {"message": "Таблица с новостями удалена успешно"}
