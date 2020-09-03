from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import nntplib
import atexit

from chatbotmaker import Bot, Dispatcher, Database
from chatbotmaker.database import add_relationship
from chatbotmaker.defaults.facebook import FacebookMessenger, facebook_route
from chatbotmaker.defaults.dev import DevMessenger

from .models import database, Server, Channel
from .dispatcher_cfg import dispatcher
from .messenger import messenger, FACEBOOK_CHECK_TOKEN
from .maintenance import check_subscription_updates
from .app import app
