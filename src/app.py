from flask import Flask

app = Flask(__name__)

def hello_world():
    return "Hello World"

from services import bot_service
app.add_url_rule('/', methods=['GET'],  view_func=hello_world)
app.add_url_rule('/', methods=['POST'],  view_func=bot_service.bot_start)

import atexit
from services import scheduled_service
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_service.run_scheduled_service, trigger="interval", seconds=14400)
scheduler.add_job(func=scheduled_service.run_scheduled_cake_service, trigger="interval", seconds=5)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
