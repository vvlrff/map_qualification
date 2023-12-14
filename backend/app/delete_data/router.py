import logging
from fastapi import APIRouter, Depends, status
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
    try:
        stmt = delete(news).where(news.c.id == news_id)
    
        await session.execute(stmt)
        await session.commit()
    
        return {"status": status.HTTP_200_OK, "message": f"Новость {news_id} удалена успешно"}
    
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error_message": str(e)}

    

@router.delete("/news")
async def delete_all_news(session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(news)
        
        await session.execute(stmt)
        await session.commit()
        
        return {"status": status.HTTP_200_OK, "message": "Таблица с новостями удалена успешно"}
    
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error_message": str(e)}

