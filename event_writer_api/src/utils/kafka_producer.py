from abc import ABC, abstractmethod
from dataclasses import dataclass

from aiokafka import AIOKafkaProducer


class AbstractProducer(ABC):
    """Абстрактный класс для подключения к хранилищу."""

    @abstractmethod
    def send(self, topic: str, value: bytes, key: bytes):
        pass


@dataclass
class KafkaProducer(AbstractProducer):
    """
    Класс для кеширования в Redis
    В качестве ключа используется текущий запрошенный URL
    URL получаем из request
    """
    kafka: AIOKafkaProducer

    async def send(self, topic: str, value: bytes, key: bytes):
        await self.kafka.send(topic=topic, value=value, key=key)
