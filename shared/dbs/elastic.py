from elasticsearch import AsyncElasticsearch
from shared import settings

host_1 = f'http://{settings.ELASTIC_NODE_01}:{settings.ELASTIC_PORT}'
host_2 = f'http://{settings.ELASTIC_NODE_02}:{settings.ELASTIC_PORT}'
host_3 = f'http://{settings.ELASTIC_NODE_03}:{settings.ELASTIC_PORT}'

elastic_client = AsyncElasticsearch(hosts=[host_1, host_2, host_3])

