# -*- encoding: utf-8 -*-

from flask import Flask
from app.libs.logger import logger

app = Flask(__name__)
app.config.from_object('instance.config.Config')