from fastapi import APIRouter, Depends
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.data_collection.models import news, country


router = APIRouter(
    prefix="/delete",
    tags=["Delete"]
)


@router.delete("/news/{news_id}")
async def delete_news(news_id: int, session: AsyncSession = Depends(get_async_session)):
    # Создание запроса на удаление данных
    stmt = delete(news).where(news.c.id == news_id)
    
    # Выполнение запроса
    await session.execute(stmt)
    
    # Подтверждение транзакции
    await session.commit()
    
    return {"message": f"News {news_id} deleted successfully"}

@router.delete("/news")
async def delete_news(session: AsyncSession = Depends(get_async_session)):
    # Создание запроса на удаление данных
    stmt = delete(news)
    
    # Выполнение запроса
    await session.execute(stmt)
    
    # Подтверждение транзакции
    await session.commit()
    
    return {"message": "News deleted successfully"}

@router.delete("/countries_coordinates/{country_id}")
async def delete_news(country_id: int, session: AsyncSession = Depends(get_async_session)):
    # Создание запроса на удаление данных
    stmt = delete(country).where(country.c.id == country_id)
    
    # Выполнение запроса
    await session.execute(stmt)
    
    # Подтверждение транзакции
    await session.commit()
    
    return {"message": f"Country {country_id} deleted successfully"}

@router.delete("/countries_coordinates")
async def delete_news(session: AsyncSession = Depends(get_async_session)):
    # Создание запроса на удаление данных
    stmt = delete(country)
    
    # Выполнение запроса
    await session.execute(stmt)
    
    # Подтверждение транзакции
    await session.commit()
    
    return {"message": "Countries deleted successfully"}

