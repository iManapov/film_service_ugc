from kafka import KafkaConsumer

from core.config import kafka_conf
from src.models.message import Message


def read_kafka_data() -> list[Message]:
    consumer = KafkaConsumer(
        kafka_conf.topic_name,
        bootstrap_servers=[kafka_conf.host],
        auto_offset_reset=kafka_conf.auto_offset_reset,
        group_id=kafka_conf.group_id,
    )
    for message in consumer:
        yield Message(message.key, message.value)
