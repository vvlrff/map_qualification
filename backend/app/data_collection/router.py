from datetime import datetime
from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.data_collection.models import news, country
from app.data_collection.services import dangerous_news_guardian
from app.data_collection.services import get_guardian_news_countries

router = APIRouter(
    prefix="/collection",
    tags=["Collection"]
)


@router.get("/get_news")
async def get_news_guardian(session: AsyncSession = Depends(get_async_session)):

    query = select(country)
    result = await session.execute(query)

    data_query = result.fetchall()
    answer = []
    for i in data_query:
        answer.append(i[1])

    data = dangerous_news_guardian()

    for i in data:
        if i['title'] not in answer:
            new_title = i['title']
            new_href = i['href']
            new_date = datetime.today()

            stmt = insert(news).values(
                title=new_title,
                href=new_href,
                date=new_date
            )

            await session.execute(stmt)
            await session.commit()

    return status.HTTP_200_OK

@router.get("/get_countries")
async def get_countries_coordinates(session: AsyncSession = Depends(get_async_session)):

    query = select(country)
    result = await session.execute(query)

    data_query = result.fetchall()
    answer = []
    for i in data_query:
        answer.append(i[1])

    data = get_guardian_news_countries()
    
    for i in data:
        if i['text'] not in answer:
            new_country = i['country']
            new_text = i['text']
            new_date = datetime.today()

            stmt = insert(country).values(
                country=new_country,
                text=new_text,
                date=new_date
            )

            await session.execute(stmt)
            await session.commit()
    
    return status.HTTP_200_OK