import os
import json
from flask import request
from common.get_bot import get_bot
from .start_message import start_message
from .default_message import default_message
from services.pos_service.get_staking_projects import get_staking_projects
from services.pos_service.get_staking_project_by_asset_name import get_staking_project_by_asset_name

def bot_start():
    update = request.get_json()
    chat_id = update["message"]["chat"]["id"]
    received_message = update["message"]["text"]
    try:
        bot = get_bot()
        
        if received_message.startswith('/t_'): # Custom route handlers
            get_staking_project_by_asset_name(bot, chat_id, received_message[3:])
        else: # Plain route handlers
            routes = {
                "/start": start_message,
                "/letsgo": get_staking_projects,
            }
            func = routes.get(received_message, default_message)
            func(bot, chat_id)

    except Exception as ex:
        print(ex)
    return "Message sent!"