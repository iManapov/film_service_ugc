import uuid

from http import HTTPStatus
from http.client import HTTPException

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import JWTDecodeError, MissingTokenError
from kafka import KafkaProducer

from pydantic import BaseModel


class Item(BaseModel):
    event_time: str


# Объект router, в котором регистрируем обработчики
router = APIRouter()
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


@router.post('/{film_id}/event',
            )
async def event_handler(film_id: uuid.UUID,
                body: Item,
                token: HTTPAuthorizationCredentials = Depends(HTTPBearer(bearerFormat='Bearer')),
                authorize: AuthJWT = Depends()
    ):
    """
    Записывает временную метку unix timestamp, на которой сейчас находится пользователь при просмотре фильма.
    """
    try:
        authorize.jwt_required()
    except JWTDecodeError:
        raise HTTPException(HTTPStatus.UNPROCESSABLE_ENTITY)
                            #detail=error_msgs.non_valid_token)
    except MissingTokenError:
        raise HTTPException(HTTPStatus.UNAUTHORIZED)
                            #detail=error_msgs.authorized_only)
    token = authorize.get_raw_jwt()
    producer.send(
        topic='views',
        value=bytearray(body.event_time, 'utf-8'),
        key=bytearray(token['user_uuid'] + "+" + str(film_id), 'utf-8'),
    )
    return {"msg": "event time successfully sent"}, HTTPStatus.OK
