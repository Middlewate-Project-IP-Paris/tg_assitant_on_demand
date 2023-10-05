# import requests
import telebot
import json
import vars
from datetime import datetime
import math
import publisher
import schedule
import time


class BotConnection:
    def __init__(self):
        self.url = telebot.TeleBot(vars.TOKEN)

    def getchatmembers(self, chat_id):
        unit_dict = {
            'moment': math.floor(datetime.timestamp(datetime.now())),
            'channel_id': chat_id,
            'subsCount': self.url.get_chat_member_count(chat_id)
        }
        k = publisher.Publisher()
        k.send2kafka(vars.KAFKA_SUBS_COUNT_TOPIC, unit_dict)

    def getchannelmeta(self, chat_id):
        unit_dict = {
            'moment': math.floor(datetime.timestamp(datetime.now())),
            'channel_id': chat_id,
            'channel_name': self.url.get_chat(chat_id).username,
            'channel_title': self.url.get_chat(chat_id).title,
            'channel_description': self.url.get_chat(chat_id).bio
        }
        k = publisher.Publisher()
        k.send2kafka(vars.KAFKA_CHANNEL_META_TOPIC, unit_dict)

    def getpoststat(self, chat_id, post_id):
        unit_dict = {
            'moment': math.floor(datetime.timestamp(datetime.now())),
            'channel_id': chat_id,
            'post_id': post_id,
            'views': self.url.post(chat_id).username,
            'channel_title': self.url.get_chat(chat_id).title,
            'channel_description': self.url.get_chat(chat_id).bio
        }
        k = publisher.Publisher()
        k.send2kafka(vars.KAFKA_CHANNEL_META_TOPIC, unit_dict)
# response = requests.get(
#    f'''{vars.TG_URL}{vars.TOKEN}{vars.MEMBER_COUNT_METHOD}{vars.CHAT_ID}''')

# print(response.content)

bot = telebot.TeleBot(vars.TOKEN)

# print(bot.get_chat_member_count(vars.CHAT_ID))
a = bot.create_chat_invite_link(vars.CHAT_ID).invite_link


json_object = json.dumps(unit_dict)
print(json_object)




