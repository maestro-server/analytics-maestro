
from app import celery


@celery.task(name="send.server")
def task_send_to_server_app(svg, token, uid):

    return {'cardials': ""}