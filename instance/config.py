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

    WS_SECRET = os.environ.get("MAESTRO_WEBSOCKET_SECRET", "wsSecretKey")
    SECRETJWT = os.environ.get("MAESTRO_SECRETJWT_ANALYTICS", "defaultSecretKey")
    NOAUTH = os.environ.get("MAESTRO_NOAUTH", "defaultSecretNoAuthToken")

    MAESTRO_DATA_URI = os.environ.get("MAESTRO_DATA_URI", "http://localhost:5010")
    MAESTRO_ANALYTICS_FRONT_URI = os.environ.get("MAESTRO_ANALYTICS_FRONT_URI", "http://localhost:9999")
    MAESTRO_WEBSOCKET_URI = os.environ.get("MAESTRO_WEBSOCKET_URI", "http://localhost:8000")

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'amqp://localhost')
    CELERY_DEFAULT_QUEUE = 'analytics'

    CELERYD_TASK_TIME_LIMIT = os.environ.get("CELERYD_TASK_TIME_LIMIT", 60)
    CELERYD_TASK_SOFT_TIME_LIMIT = os.environ.get("CELERYD_TASK_SOFT_TIME_LIMIT", 1080)