def default_message(bot, chat_id):
    message = "I don't understand sir."
    bot.send_message(chat_id=chat_id, text=message)