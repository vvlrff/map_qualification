from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.elastic import elastic_client
from app.database import get_async_session
from app.data_collection.models import news

router = APIRouter(
    prefix="/elasticsearch",
    tags=["Elasticsearch"]
)


@router.get("/migration_from_db")
async def migration_from_db(session: AsyncSession = Depends(get_async_session)):

    query = select(news)
    result = await session.execute(query)

    data = result.fetchall()

    for i in data:
        news_title = i[1]
        news_href = i[2]
        news_country = i[4]
        news_city = i[5]
        news_image = i[3]
        news_date = i[6]

        document = {
            'title': news_title,
            'href': news_href,
            'country': news_country,
            'city': news_city,
            'image': news_image,
            'date': news_date
        }
        
        await elastic_client.index(index='news', document=document)
    
    search_results = await elastic_client.search(
        index='news',
        query={
            "match_all": {}
        },
        _source=["title", "href", "country", "city", "image", "date"]
    )

    return {"status": status.HTTP_200_OK, "result": search_results}


@router.get("/get_elastic_data")
async def get_elastic_data():
    search_results = await elastic_client.search(
        index='news',
        query={
            "match_all": {}
        },
        _source=["title", "href", "country", "city", "image", "date"]
    )
    return {"status": status.HTTP_200_OK, "result": search_results}


@router.get("/search_{search}")
async def search_by_title(search: str):
    search_params = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "title": {
                                "query": search,
                                "operator": "and",
                                "fuzziness": 'AUTO'
                            }
                        }
                    }
                ]
            }
        }
    }

    try:
        search_results = await elastic_client.search(index='news', body=search_params)
        hits = search_results['hits']['hits']

        return {"results": hits, "status": status.HTTP_200_OK }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
