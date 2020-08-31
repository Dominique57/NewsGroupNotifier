from . import Dispatcher


new_paths = ['help', 'subscribe']
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


dispatcher_config = {
    'actions': {
        'welcome': Dispatcher.DEFAULT,
        'home': Dispatcher.DEFAULT,
    }
}
dispatcher_env = globals()
