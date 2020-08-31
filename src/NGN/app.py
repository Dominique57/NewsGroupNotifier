""" App front-end """
from . import Flask, request, Bot, bot, facebook_route, FACEBOOK_CHECK_TOKEN


app = Flask(__name__)


@app.route('/bot', methods=['GET', 'POST'])
def ngn_bot():
    return facebook_route(request, FACEBOOK_CHECK_TOKEN, bot)


@app.route('/bot_debug', methods=['GET'])
def ngn_bot_debug():
    if request.method == 'GET':
        user_id = request.args.get("user")
        user_input = request.args.get("message")
        return bot.user_handle(user_id, user_input)
    return "Message ignored"
