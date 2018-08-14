
import json
from app.libs.jwt import Jwt
from app import celery
from .notification import task_notification
from app.repository.externalMaestroAnalyticsFront import ExternalMaestroAnalyticsFront

@celery.task(name="send.server")
def task_send_to_server_app(owner_id, graph_id, svg):

    try:
        token = Jwt.create_tkn(graph_id, owner_id)
        access = Jwt.encode(token)
    except Exception as error:
        print(str(error))
        task_notification(owner_id=owner_id, msg=str(error), status="danger")

    headers = {
        'Authorization': 'JWT %s' % access.decode("utf-8")
    }

    ExternalRequest = ExternalMaestroAnalyticsFront(owner_id=owner_id)
    ExternalRequest.set_headers(headers)
    result = ExternalRequest.post_request(path="graphs", body={'payload': svg})

    return {'result': result, 'graph_id': graph_id, 'owner_id': owner_id}