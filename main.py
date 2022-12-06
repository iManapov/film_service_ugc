import logging
import sys
import os
import aioredis
import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi_jwt_auth import AuthJWT
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.api.v1 import films
from src.core.config import settings

# Создание FastAPI приложения
app = FastAPI(
    title='name',
    description="Информация о фильмах, жанрах и людях, участвовавших в создании произведения",
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    version='1.0.0'
)


# @app.on_event('startup')
# async def startup():
#     # Подключаемся к базам при старте сервера
#     elastic.es = AsyncElasticsearch(
#         hosts=[f'{settings.elastic_host}:{settings.elastic_port}']
#     )
#
#     redis.redis = await aioredis.create_redis_pool(
#         (settings.redis_host, settings.redis_port),
#         minsize=10,
#         maxsize=20
#     )


# @app.on_event('shutdown')
# async def shutdown():
#     # Отключаемся от баз при выключении сервера
#     await redis.redis.close()
#     await elastic.es.close()

# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return settings

# Подключаем роутер к серверу, указав префикс /v1/films
app.include_router(films.router, prefix='/api/v1/films', tags=['films'])


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
    )
