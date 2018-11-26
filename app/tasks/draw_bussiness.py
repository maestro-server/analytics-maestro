
from app import celery
from app.libs.drawing.layoutSVG import DrawLayout

from .send_front_app import task_send_to_front_app


@celery.task(name="draw.bussiness")
def task_draw_bussiness(owner_id, graph_id, grid, index, edges):

    Layout = DrawLayout(grid, index)

    Layout.draw_connections(edges)
    Layout.draw_nodes()
    xml = Layout.save()

    payload = {
        'payload': xml,
        'total': len(index)
    }

    send_app_id = task_send_to_front_app.delay(owner_id, graph_id, payload)

    return {'send_app_id': str(send_app_id), 'graph_id': graph_id, 'owner_id': owner_id}