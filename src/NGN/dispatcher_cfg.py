from . import Dispatcher, Channel, Server
from .tools import *


new_paths = {
    'subscribe': 'subscribe_server',
}
help_message = 'Here are available commands:\n -' + '\n -'.join(new_paths)


def func_welcome(user, user_input):
    user.send_message('Hello and welcome to NewsGroupNotifier')
    user.change_state('home')
    user.execute_handle(user_input)

def pre_func_home(user):
    user.send_message('You are in the home state!')

def func_home(user, user_input):
    user_input = user_input.lower()
    if user_input in new_paths:
        user.change_state(user_input)
    else:
        user.send_message(help_message)

def enter_func_subscribe_server(user):
    user.send_message('Please input the address of the wanted server:')

def func_subscribe_server(user, user_input):
    if is_ntp_addres_valid(user_input):
        user.store_argument('server_address', user_input)
        user.change_state('subscribe_channel')
    else:
        user.send_message('The address is invalid!')

def enter_func_subscribe_channel(user):
    user.send_message('Please input the address of the wanted channel:')

def func_subscribe_channel(user, user_input):
    server_address = user.get_argument('server_address')
    if is_ntp_channel_valid(server_address, user_input):
        user.send_message('Your subscription has been accepted!')
        user.change_state('home')
    else:
        user.send_message('The address is invalid!')


dispatcher_config = {
    'actions': {
        'welcome': Dispatcher.DEFAULT,
        'home': Dispatcher.DEFAULT,
        'subscribe_server': Dispatcher.DEFAULT,
        'subscribe_channel': Dispatcher.DEFAULT,
    }
}
dispatcher = Dispatcher(dispatcher_config, globals())
