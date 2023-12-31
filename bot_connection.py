# import requests
import pytz
import telebot
import json
import vars
import datetime
from datetime import datetime as dt
import math
import publisher
import schedule
import time
import random
import string


def get_random_string(length):
    letters = string.ascii_letters
    result = ''.join(random.choice(letters) for i in range(length))
    return result


class BotConnection:
    def __init__(self):
        self.url = telebot.TeleBot(vars.TOKEN)

    def getchatmembers(self, chat_id):
        unit_dict = {
            'moment': str(math.floor(dt.timestamp(dt.now()))),
            'channel_id': chat_id,
            'subsCount': 50#self.url.get_chat_member_count(chat_id)
        }
        k = publisher.Publisher()
        print('Connected to kafka subsCount \n')
        k.send2kafka(vars.KAFKA_SUBS_COUNT_TOPIC, unit_dict)

    def getchannelmeta(self, chat_id):
        unit_dict = {
            'moment': str(math.floor(dt.timestamp(dt.now()))),
            'channel_id': chat_id,
            'channel_name': get_random_string(10),#self.url.get_chat(chat_id).username,
            'channel_title': get_random_string(30), #self.url.get_chat(chat_id).title,
            'channel_description': get_random_string(40)#self.url.get_chat(chat_id).bio
        }
        k = publisher.Publisher()
        print('Connected to kafka channelMeta \n')
        k.send2kafka(vars.KAFKA_CHANNEL_META_TOPIC, unit_dict)

    def getpoststat(self, chat_id, post_id):
        d = dt.timestamp(dt.utcnow().replace(tzinfo=pytz.utc))
        unit_dict = {
            'moment': str(math.floor(dt.timestamp(dt.now()))),
            'channel_id': chat_id,
            'post_id': post_id,
            'views': 100, #self.url.post(chat_id).username,
            'shares': 100,
            'publicated_at': str(d),
            'edited_at': str(d),
            'deleted_at': str(d),
        }
        k = publisher.Publisher()
        print('Connected to kafka postStats \n')
        k.send2kafka(vars.KAFKA_POST_STAT_TOPIC, unit_dict)

    def getpost(self, chat_id, post_id):
        d = dt.timestamp(dt.utcnow().replace(tzinfo = pytz.utc))
        unit_dict = {
            'moment': str(math.floor(dt.timestamp(dt.now()))),
            'channel_id': chat_id,
            'post_id': post_id,
            'content': get_random_string(100),  # self.url.post(chat_id).username,
            'attachments': [get_random_string(10), get_random_string(50)], #self.url.get_chat(chat_id).title,
            'publicated_at': str(d) #self.url.get_chat(chat_id).bio
        }
        k = publisher.Publisher()
        print('Connected to kafka postContent \n')
        k.send2kafka(vars.KAFKA_POST_CONTENT_TOPIC, unit_dict)

    def joinchannel(self, url):
        id = ''
        for letter in url:
            if letter.isdigit():
                id = id + letter
        try:
            chat_id = int(id)
            self.getchannelmeta(chat_id)
        except ValueError:
            print("Invalid Link \n")



# response = requests.get(
#    f'''{vars.TG_URL}{vars.TOKEN}{vars.MEMBER_COUNT_METHOD}{vars.CHAT_ID}''')

# print(response.content)

#bot = telebot.TeleBot(vars.TOKEN)

# print(bot.get_chat_member_count(vars.CHAT_ID))
#a = bot.create_chat_invite_link(vars.CHAT_ID).invite_link


#json_object = json.dumps(unit_dict)
#print(json_object)




