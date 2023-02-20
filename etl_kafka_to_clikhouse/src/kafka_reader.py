from abc import ABC, abstractmethod

from kafka import KafkaConsumer, errors as kafka_errors

from core.config import KafkaSettings
from src.models.message import Message
from src.backoff import backoff


class AbstractReader(ABC):
    """Abstract class for consumer"""

    @abstractmethod
    def read_data(self) -> list[Message]:
        pass

    @abstractmethod
    def commit(self):
        pass


class KafkaReader(AbstractReader):
    """Kafka consumer"""

    def __init__(self, conf: KafkaSettings):
        self.__conf = conf
        self.__consumer = None
        self.__connect()

    @backoff(error=kafka_errors.NoBrokersAvailable)
    def __connect(self):
        self.__consumer = KafkaConsumer(
            self.__conf.topic_name,
            bootstrap_servers=[self.__conf.host],
            auto_offset_reset=self.__conf.auto_offset_reset,
            enable_auto_commit=self.__conf.enable_auto_commit,
            group_id=self.__conf.group_id,
        )

    def read_data(self) -> list[Message]:
        """
        Yields messages from Kafka

        :return: list of messages
        """
        for message in self.__consumer:
            yield Message(message.key, message.value)

    def commit(self):
        """Commits message read"""

        self.__consumer.commit()
