
from app import celery

@celery.task(name="send.server")
def task_send_to_server_app(svg):
    print(svg)

    #ExternalRequest = ExternalMaestroData(owner_id=owner_id)
    #result = ExternalRequest.get_request(path="servers", query=query)

    return {'cardials': ""}