from fastapi import APIRouter, HTTPException, status
from app.elastic import elastic_client


router = APIRouter(
    prefix="/elasticsearch",
    tags=["Elasticsearch"]
)


@router.get("/get_elastic_data")
async def get_elastic_data():
    search_results = await elastic_client.search(
        index='news',
        query={
            "match_all": {}
        },
        _source=["title", "href", "country", "city", "image", "date"]
    )
    return {"success": True, "result": search_results}


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

        return {"results": hits, "status": status.HTTP_200_OK, }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
