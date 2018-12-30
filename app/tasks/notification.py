
from app.views import app
from app import celery
from app.repository.externalMaestro import ExternalMaestro
from app.services.privateAuth.decorators.external_private_token import create_jwt

@celery.task(name="notification.api")
def task_notification(graph_id, msg=None, status=None, more={}):

    data = {'_id': graph_id}

    if status:
        data['status'] = status

    if msg:
        data['msg'] = msg


    merged = {**data, **more}

    base = app.config['MAESTRO_DATA_URI']
    ExternalMaestro(base) \
        .set_headers(create_jwt()) \
        .put_request(path="graphs", body={'body': [merged]})

    return {'graph_id': graph_id}
