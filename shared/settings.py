# if you want to use this settings, please include "shared" requirements.txt in your subproject
# it can be done by adding "-r ../shared/requirements.txt" line to your requirements.txt

# don't forget to add shared requirements.txt to your Docker container!
from pathlib import Path

from dotenv import load_dotenv
from envparse import env

load_dotenv(env('DOTENV_FILE', default='.env.dev'))
# load_dotenv(env('DOTENV_FILE', default='.env'))

BASE_DIR = Path(__file__).resolve().parent.parent


# postgresql
PG_USERNAME = env('POSTGRES_USER')
PG_PASSWORD = env('POSTGRES_PASSWORD')
PG_HOST = env('DB_HOST', default='127.0.0.1')
PG_PORT = env.int('DB_PORT', default=5432)
PG_DB = env('POSTGRES_DB')
PG_PROTOCOL = env('POSTGRES_PROTOCOL', default='postgresql+asyncpg')
PG_URI_QUERY = env('POSTGRES_URI_QUERY', default=str())

# mongo
MONGO_USERNAME = env('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASSWORD = env('MONGO_INITDB_ROOT_PASSWORD')
MONGO_HOST = env('MONGO_HOST', default='127.0.0.1')
MONGO_PORT = env.int('MONGO_PORT', default=27017)
MONGO_URI_QUERY = env('MONGO_URI_QUERY', default=str())
MONGO_PROTOCOL = env('MONGO_PROTOCOL', default='mongodb')

# rabbitmq
RABBITMQ_USERNAME = env('RABBIT_USER', default='guest')
RABBITMQ_PASSWORD = env('RABBIT_PASSWORD', default='guest')
RABBITMQ_HOST = env('RABBIT_HOST', default='127.0.0.1')
RABBITMQ_PORT = env.int('RABBIT_PORT', default=5672)
RABBITMQ_PROTOCOL = env('RABBIT_PROTOCOL', default='amqp')
RABBITMQ_URI_QUERY = env('RABBIT_URI_QUERY', default=str())

# parser
MONGO_PARSER_DB_NAME = env('MONGO_PARSER_DB')
MONGO_PARSER_NEWS_COLLECTION = env('MONGO_PARSER_NEWS_COLLECTION')
PARSER_RABBITMQ_QUEUE_NAME = env('RABBIT_PARSER_QUEUE', default='parser')
PARSER_MIN_WORD_COUNT = env.int('PARSER_MIN_WORD_COUNT', default=5)

# elastic
ELASTIC_PORT=env('ELASTIC_HOST', default=9200)
ELASTIC_NODE_01=env('ELASTIC_NODE_01')
ELASTIC_NODE_02=env('ELASTIC_NODE_02')


