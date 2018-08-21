
from app.views import app
from app import celery
from app.repository.externalMaestro import ExternalMaestro

@celery.task(name="notification.api")
def task_notification(owner_id, graph_id, msg, status='success', more={}):

    data = {'_id': graph_id, 'status': status, 'msg': msg}
    merged = {**data, **more}

    base = app.config['MAESTRO_DATA_URI']
    status = ExternalMaestro(base)\
                            .put_request(path="graphs", body={'body': [merged]})

    return {'owner_id': owner_id, 'status': status}
