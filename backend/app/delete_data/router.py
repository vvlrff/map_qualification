from fastapi import APIRouter, Depends
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.data_collection.models import news


router = APIRouter(
    prefix="/delete",
    tags=["Delete"]
)


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


