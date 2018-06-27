import requests
from app import celery
from app.libs.logger import logger
from app.libs.url import FactoryDataURL
from app.libs.statusCode import check_status


@celery.task(name="notification.api")
def task_notification(owner_id, msg, status='success', more={}):
    role = {'_id': owner_id, 'role': 5}

    data = {'roles': [role], 'status': status, 'msg': msg, 'context': 'analytics', 'active': True}
    merged = {**data, **more}

    path = FactoryDataURL.make(path="events")
    context = requests.put(path, json={'body': [merged]})

    if check_status(context):
        logger.error("Reports: TASK [notification] - %s", context.text)

    return {'owner_id': owner_id, 'status': context.status_code}
