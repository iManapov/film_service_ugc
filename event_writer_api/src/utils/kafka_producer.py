from abc import ABC, abstractmethod
from dataclasses import dataclass

from aiokafka import AIOKafkaProducer


class AbstractProducer(ABC):
    """Producer abstract class"""

    @abstractmethod
    def send(self, topic: str, value: bytes, key: bytes):
        """Sends message to queue"""
        pass


@dataclass
class KafkaProducer(AbstractProducer):
    """Kafka producer class"""

    kafka: AIOKafkaProducer

    async def send(self, topic: str, value: bytes, key: bytes):
        """
        Sends message to Kafka

        :param topic: topic name in Kafka
        :param value: message body
        :param key: message key
        """

        await self.kafka.send(topic=topic, value=value, key=key)
