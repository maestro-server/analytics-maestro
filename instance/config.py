# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import os
from app.libs.jsonEncoder import DateTimeEncoder
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    TESTING = os.environ.get("TESTING", False)
    RESTFUL_JSON = {'cls': DateTimeEncoder}

    SECRETJWT = os.environ.get("MAESTRO_SECRETJWT", "defaultSecretKey")
    NOAUTH = os.environ.get("MAESTRO_NOAUTH", "defaultSecretNoAuthToken")

    MAESTRO_DATA_URI = os.environ.get("MAESTRO_DATA_URI", "http://localhost:5010")
    MAESTRO_ANALYTICS_FRONT_URI = os.environ.get("MAESTRO_ANALYTICS_FRONT_URI", "http://localhost:9999")
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'amqp://localhost')
    CELERY_DEFAULT_QUEUE = 'analytics'
    CELERYD_TASK_SOFT_TIME_LIMIT = 1080
    

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    CELERYD_MAX_TASKS_PER_CHILD = 1
    DEBUG = True


class TestingConfig(Config):
    CELERYD_MAX_TASKS_PER_CHILD = 1
    TESTING = True
