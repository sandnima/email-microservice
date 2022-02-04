import asyncio
import json
import os

from aiokafka import AIOKafkaConsumer
from smtp import send_email
from utils import deserializer

# env variables
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'email_send')
KAFKA_CONSUMER_GROUP = os.getenv('KAFKA_CONSUMER_GROUP', 'email_send')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# global variables
loop = asyncio.new_event_loop()


async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=KAFKA_CONSUMER_GROUP,
        auto_offset_reset='earliest'
    )
    await consumer.start()
    try:
        # consume messages
        async for msg in consumer:
            try:
                # deserialize
                msg_value = deserializer(msg.value)
                # send email
                send_email(**msg_value)
            except json.decoder.JSONDecodeError as e:
                print(f"Bad json format:\n{e}")
            except AssertionError:
                print(f"Assertion error happened")
            print(f"Consumed msg: {msg}")
    finally:
        await consumer.stop()


loop.run_until_complete(consume())
