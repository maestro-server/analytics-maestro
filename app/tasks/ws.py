
from app import celery
from app.repository.externalMaestroWS import ExternalMaestroWS

@celery.task(name="ws.api")
def task_ws(graph_id, owner_id, status='success'):
    title = "Finish Graph"
    msg = "(%s)" % (graph_id)
    channel = "maestro-%s" % owner_id

    body = {
        "method": "publish",
        "params": {
            "channel": channel,
            "data": {
                "notify": {
                    "title": title,
                    "msg": msg,
                    "type": status
                },
                "event": {
                    "caller": ["analytics-update", "analytics-{}".format(graph_id)]
                }
            }
        }
    }

    result = ExternalMaestroWS()\
        .auth_header()\
        .post_request(path="api", body=body)\
        .get_results()

    return {'result': result, 'task': 'ws-notification'}