
from app import celery
from app.libs.drawing.layoutSVG import DrawLayout


@celery.task(name="send.server")
def task_send_to_server_app(svg, token, uid):

    return {'cardials': ""}