""" App front-end """
from . import Flask, request, Bot, facebook_route, FACEBOOK_CHECK_TOKEN,\
              check_subscription_updates, BackgroundScheduler, atexit
from . import database, dispatcher, messenger


app = Flask(__name__)
bot = Bot({}, messenger, dispatcher, database)


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


# Check for new message every
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_subscription_updates, trigger='interval',
                  seconds=60*5)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())
