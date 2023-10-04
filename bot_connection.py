# import requests
import telebot
import json
import vars
from datetime import datetime
import math
from json import dumps
from kafka import KafkaProducer
import schedule
import time

# response = requests.get(
#    f'''{vars.TG_URL}{vars.TOKEN}{vars.MEMBER_COUNT_METHOD}{vars.CHAT_ID}''')

# print(response.content)

bot = telebot.TeleBot(vars.TOKEN)

# print(bot.get_chat_member_count(vars.CHAT_ID))
a = bot.create_chat_invite_link(vars.CHAT_ID).invite_link


def one_job():
    unit_dict = {
        'timestamp': math.floor(datetime.timestamp(datetime.now())),
        'channel_id': vars.CHAT_ID,
        'number_of_followers': bot.get_chat_member_count(vars.CHAT_ID)
    }

    json_object = json.dumps(unit_dict)
    print(json_object)

    producer = KafkaProducer(bootstrap_servers=[vars.KAFKA_BROKER],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))

    producer.send(vars.TOPIC_SUBS, value=unit_dict)


schedule.every(10).minutes.do(one_job)

while True:
    schedule.run_pending()
    time.sleep(1)
