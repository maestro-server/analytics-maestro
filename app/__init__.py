# -*- encoding: utf-8 -*-

from flask import Flask
from .celery import make_celery
from app.libs.logger import logger


app = Flask(__name__)
app.config.from_object('instance.config.Config')

celery = make_celery(app)

from app import views