
from app.libs.jwt import Jwt
from app import celery
from app.libs.logger import logger
from app.repository.externalMaestroAnalyticsFront import ExternalMaestroAnalyticsFront
from .notification import task_notification

@celery.task(name="send.server")
def task_send_to_front_app(owner_id, graph_id, payload):

    try:
        token = Jwt.create_tkn(graph_id, owner_id)
        access = Jwt.encode(token)
    except Exception as error:
        logger.error(error)
        task_notification.delay(graph_id=graph_id, owner_id=owner_id, msg=str(error), status="danger")

    headers = {
        'Authorization': 'JWT %s' % access.decode("utf-8")
    }

    ExternalRequest = ExternalMaestroAnalyticsFront(owner_id=owner_id, graph_id=graph_id)
    ExternalRequest.set_headers(headers)
    result = ExternalRequest.post_request(path="graphs", body=payload)

    return {'result': result, 'graph_id': graph_id, 'owner_id': owner_id}