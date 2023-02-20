from pydantic import BaseModel
import orjson


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class JsonMixin(BaseModel):
    """Faster class to work with json"""

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class EventBody(JsonMixin):
    """Event model"""

    event_time: int


class EventResponse(JsonMixin):
    """Event response"""

    msg: str
