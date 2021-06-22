import os
import json
from telegram import Bot
from flask import request
from services import pos_service

def get_bot():
    bot = Bot("1832535976:AAFlFCrIZYWTwfnvYjh5ZPvGnQSuoe3OJQ0")
    return bot

def hello_world():
    return "Hello, World!"

def bot_start():
    update = request.get_json()
    received_message = update["message"]["text"]
    try:
        bot = get_bot()

        message = ""
        if received_message == '/start':
            message += "Hi my name is Binance PoS Alert Bot!"
        elif received_message == '/letsgo':
            message += str(pos_service.get_staking_projects())
        else:
            message += "I don't understand sir."

        bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
    except Exception as ex:
        print(ex)
    return "Message sent!"