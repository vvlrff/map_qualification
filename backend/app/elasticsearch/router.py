from fastapi import APIRouter, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from app.elastic import elastic_client
from app.database import get_async_session
from app.data_collection.models import news
from app.elasticsearch.schemas import InputUserMessage, InputUserMessageDate
import logging

router = APIRouter(
    prefix="/elasticsearch",
    tags=["Elasticsearch"]
)


def answer_transformation(result):
    elastic_answer = []
    for el in result:
        elastic_answer.append({
            'title_en': el['_source']['title_en'],
            'title_ru': el['_source']['title_ru'],
            'href': el['_source']['href'],
            'date': el['_source']['date'],
            'image': f"http://localhost:8000/photos/{el['_source']['image']}",
            'topical_keywords': el['_source']['topical_keywords'],
            'country': el['_source']['country'],
            'city': el['_source']['city'],
            'relevant_score': el['_score'],
        })

    return elastic_answer


@router.post("/create_elastic_index")
async def create_elastic_index():
    try:
        index_settings = {
            "settings": {
                "analysis": {
                    "analyzer": {
                        "news_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": [
                                "lowercase",
                                "russian_stop",
                                "russian_stemmer"
                            ]
                        },
                        "english_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": [
                                "lowercase",
                                "english_stop",
                                "english_stemmer"
                            ]
                        }
                    },
                    "filter": {
                        "russian_stop": {
                            "type": "stop",
                            "stopwords": "_russian_"
                        },
                        "russian_stemmer": {
                            "type": "stemmer",
                            "language": "russian"
                        },
                        "english_stop": {
                            "type": "stop",
                            "stopwords": "_english_"
                        },
                        "english_stemmer": {
                            "type": "stemmer",
                            "language": "english"
                        },
                    }
                }
            },
            "mappings": {
                "properties": {
                    "id": {"type": "integer"},
                    "date": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                    "title_ru": {"type": "text", "analyzer": "news_analyzer"},
                    "title_en": {"type": "text", "analyzer": "english_analyzer"},
                    "href": {"type": "text"},
                    "image": {"type": "text"},
                    "country": {"type": "text"},
                    "city": {"type": "text"},
                    "topical_keywords": {"type": "text"}
                }
            }
        }

        await elastic_client.indices.create(index='news_index', body=index_settings)

        return {"status": status.HTTP_200_OK, "result": "Индекс создан"}

    except Exception as e:
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error_message": str(e)}


@router.get("/migration_from_db")
async def migration_from_db(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(news)
        result = await session.execute(query)

        data = result.fetchall()

        for i in data:
            news_id = i[0]
            news_title_en = i[1]
            news_title_ru = i[2]
            news_href = i[3]
            news_image = i[4]
            news_country = i[5]
            news_city = i[6]
            news_topical_keywords = i[7]
            news_date = i[8]

            news_date = i[8].isoforббблобббоmat()


            document = {
                'id': news_id,
                'title_en': news_title_en,
                'title_ru': news_title_ru,
                'href': news_href,
                'image': news_image,
                'country': news_country,
                'city': news_city,
                'topical_keywords': news_topical_keywords,
                'date': news_date,
            }

            await elastic_client.index(index='news_index', document=document)

        return {"status": status.HTTP_200_OK, "result": "Миграция прошла успешно"}

    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error_message": str(e)}


@router.get("/get_elastic_data")
async def get_elastic_data():
    try:
        search_results = await elastic_client.search(
            index='news_index',
            query={
                "match_all": {}
            },
        )
        hits = search_results['hits']['hits']
        return {"status": status.HTTP_200_OK, "result": answer_transformation(hits)}

    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error_message": str(e)}


@router.post("/search")
async def search_by_title(search: InputUserMessage):
    try:
        search_params_en = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "title_en": {
                                    "query": search.message,
                                    "operator": "and",
                                    "fuzziness": 'AUTO'
                                }
                            }
                        }
                    ]
                }
            }
        }

        search_results_en = await elastic_client.search(index='news_index', body=search_params_en)

        search_params_ru = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "title_ru": {
                                    "query": search.message,
                                    "operator": "and",
                                    "fuzziness": 'AUTO'
                                }
                            }
                        }
                    ]
                }
            }
        }

        search_results_ru = await elastic_client.search(index='news_index', body=search_params_ru)

        hits_en = search_results_en['hits']['hits']
        hits_ru = search_results_ru['hits']['hits']

        combined_results = hits_en + hits_ru

        return {"results": answer_transformation(combined_results), "status": status.HTTP_200_OK}

    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error_message": str(e)}


@router.post("/search_by_date")
async def search_by_title_and_date(search: InputUserMessageDate):
    try:
        search_params_en = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "title_en": {
                                    "query": search.message,
                                    "operator": "and",
                                    "fuzziness": 'AUTO'
                                }
                            }
                        },
                        {
                            "range": {
                                "date": {
                                    "gte": search.begin,
                                    "lte": search.end
                                }
                            }
                        }
                    ]
                }
            }
        }

        search_results_en = await elastic_client.search(index='news_index', body=search_params_en)

        search_params_ru = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "title_ru": {
                                    "query": search.message,
                                    "operator": "and",
                                    "fuzziness": 'AUTO'
                                }
                            }
                        },
                        {
                            "range": {
                                "date": {
                                    "gte": search.begin,
                                    "lte": search.end
                                }
                            }
                        }
                    ]
                }
            }
        }

        search_results_ru = await elastic_client.search(index='news_index', body=search_params_ru)

        hits_en = search_results_en['hits']['hits']
        hits_ru = search_results_ru['hits']['hits']

        combined_results = hits_en + hits_ru

        return {"results": answer_transformation(combined_results), "status": status.HTTP_200_OK}

    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "error_message": str(e)}
