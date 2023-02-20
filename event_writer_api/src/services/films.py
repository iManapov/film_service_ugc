from fastapi import Depends
from aiokafka import AIOKafkaProducer

from src.db.kafka import get_kafka
from src.utils.kafka_producer import AbstractProducer
from src.utils.kafka_producer import KafkaProducer


class EventService:
    """Kafka event service"""

    def __init__(self, kafka: AbstractProducer):
        self.kafka = kafka

    async def send_event(self, topic: str, value: bytes, key: bytes):
        """
        Sends event to Kafka

        :param topic: topic name in Kafka
        :param value: message body
        :param key: message key
        """

        await self.kafka.send(topic=topic, value=value, key=key)


def get_event_service(
        kafka: AIOKafkaProducer = Depends(get_kafka)
) -> EventService:
    """
    EventService provider
    using 'Depends', it says that it needs AIOKafkaProducer
    """
    return EventService(KafkaProducer(kafka))
