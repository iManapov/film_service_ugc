from fastapi import Depends
from aiokafka import AIOKafkaProducer

from src.db.kafka import get_kafka
from src.utils.kafka_producer import AbstractProducer
from src.utils.kafka_producer import KafkaProducer


class EventService:
    def __init__(self, kafka: AbstractProducer):
        self.kafka = kafka

    async def send_event(self, topic: str, value: bytes, key: bytes):
        await self.kafka.send(topic=topic, value=value, key=key)


def get_event_service(
        kafka: AIOKafkaProducer = Depends(get_kafka)
) -> EventService:
    """
    Провайдер FilmService,
    с помощью Depends он сообщает, что ему необходимы Redis и Elasticsearch
    """
    return EventService(KafkaProducer(kafka))
