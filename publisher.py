from json import dumps
from kafka import KafkaProducer

import vars


class Publisher:

    def __init__(self):
        self.url = vars.KAFKA_BROKER

    def send2kafka(self, topic, message):
        producer = KafkaProducer(bootstrap_servers=[self.url],
                                 value_serializer=lambda x:
                                 dumps(x).encode('utf-8'))
        producer.send(topic, value=message)
