from tinydb import TinyDB

def get_db():
    return TinyDB("telegram_bot_db.json")

