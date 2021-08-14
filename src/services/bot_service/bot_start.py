import os
import json
from flask import request
from common.get_bot import get_bot
from .start_message import start_message
from .default_message import default_message
from .set_scheduled_monitoring import set_scheduled_monitoring
from services.pos_service.get_staking_projects import get_staking_projects
from services.pos_service.get_staking_project_by_asset_name import get_staking_project_by_asset_name

def bot_start():
    update = request.get_json()
    chat_id = update["message"]["chat"]["id"]
    received_message = update["message"]["text"]
    try:
        bot = get_bot()
        command = received_message.split(" ")[0]
        
        routes = {
            "/start": start_message,
            "/check_all": get_staking_projects,
            "/check": get_staking_project_by_asset_name,
            "/schedule": set_scheduled_monitoring,
        }
        func = routes.get(command, default_message)
        if func.__code__.co_argcount == 3: # Check number of parameters/arguments accepted by function
            func(bot, chat_id, received_message)
        else:
            func(bot, chat_id)

    except Exception as ex:
        print(ex)
    return "Message sent!"