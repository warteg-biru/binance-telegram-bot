from tinydb import Query
from common.get_db import get_db

def set_scheduled_monitoring(bot, chat_id, received_message):
    db = get_db()
    args = received_message.split(" ")
    
    if len(args) <= 1:
        bot.send_message(chat_id=chat_id, text="Command arguments cannot be empty!")
        return

    asset_name = args[1].upper()
    percentage = 0
    if len(args) > 2 and args[2].isnumeric(): # Expected percentage is 0 by default unless argument passed
        percentage = int(args[2])

    try:    
        User = Query()
        res = db.search(User.chat_id == chat_id)
        if len(res) ==  1:
            res[0]['scheduled'].append({
                "asset_id": asset_name,
                "percentage": percentage
            })
            db.update(res[0], User.chat_id == chat_id)
        else:
            db.insert({
                "chat_id": chat_id,
                "scheduled": [
                    {
                        "asset_id": asset_name,
                        "percentage": percentage
                    },
                ],
            })
        bot.send_message(chat_id=chat_id, text="Successfully scheduled asset monitoring request!")
    except Exception as e:
        print(e)
        bot.send_message(chat_id=chat_id, text="Failed to schedule asset monitoring request, please try again later.")