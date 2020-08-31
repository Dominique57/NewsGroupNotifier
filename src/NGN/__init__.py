from flask import Flask, request
from chatbotmaker import Bot, Dispatcher, Database
from chatbotmaker.defaults.facebook import FacebookMessenger, facebook_route
from chatbotmaker.defaults.dev import DevMessenger

from .dispatcher_cfg import dispatcher_config, dispatcher_env
from .initialization import FACEBOOK_CHECK_TOKEN, bot
from .app import app
