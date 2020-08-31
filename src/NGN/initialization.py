from . import FacebookMessenger, Dispatcher, Bot, Database, dispatcher_config,\
              dispatcher_env
from . import DevMessenger


FACEBOOK_CHECK_TOKEN = 'VERIFY_TOKEN'
FACEBOOK_AUTH_TOKEN = 'EAAKnsCzlM7wBAM0waYVmDwMFMg1s6GMDoDCXSV1ZADQ9xxhzonZAKhHmJ8TZBhN58IKd9cUlAprdc1lBPFhXmRQTmBv8aNZAq6ko2wVTwF0xxOKDkwrD2iRKeQEVzjCk2J6eNAfCzkD2uQ4rGv96QwZC24p8sZC2GrS4uv25WNgQZDZD'
# messenger = FacebookMessenger(FACEBOOK_AUTH_TOKEN)
messenger = DevMessenger()
dispatcher = Dispatcher(dispatcher_config, dispatcher_env)
database = Database({'sqlalchemy.url': 'sqlite:///foo.db'})
bot = Bot({}, messenger, dispatcher, database)
