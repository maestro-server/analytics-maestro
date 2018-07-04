
from app.views import app
from app import celery
from app.repository.externalMaestro import ExternalMaestro

@celery.task(name="notification.api")
def task_notification(owner_id, msg, status='success', more={}):
    role = {'_id': owner_id, 'role': 5}

    data = {'roles': [role], 'status': status, 'msg': msg, 'context': 'analytics', 'active': True}
    merged = {**data, **more}

    base = app.config['MAESTRO_DATA_URI']
    status = ExternalMaestro(base)\
                            .put_request(path="events", json={'body': [merged]})

    return {'owner_id': owner_id, 'status': status}
