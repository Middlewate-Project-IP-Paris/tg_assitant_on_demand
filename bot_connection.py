import requests
import telebot
import json

chat_id = -1001604616173
token = '6569366772:AAEYXf01qD2atyNslTUkzksjBTtXOJfwhZc'

response = requests.get(
    f"https://api.telegram.org/bot{token}/getChatMemberCount?chat_id={chat_id}")
print(response.content)

bot = telebot.TeleBot(token)

print(bot.get_chat_member_count(chat_id))
