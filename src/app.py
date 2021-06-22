from flask import Flask

app = Flask(__name__)

from services import bot_service
app.add_url_rule('/', methods=['GET'],  view_func=bot_service.hello_world)
app.add_url_rule('/', methods=['POST'],  view_func=bot_service.bot_start)