from pydantic import BaseModel


class EventBody(BaseModel):
    """Модель тела запроса для записи события."""
    event_time: int


class EventResponse(BaseModel):
    """Модель ответа при записи событий."""
    msg: str
