
from app import celery
from app.libs.drawing.layoutSVG import DrawLayout
from .send_server_app import task_send_to_server_app


@celery.task(name="draw.bussiness")
def task_draw_bussiness(owner_id, grid, index, edges, servers):

    Layout = DrawLayout(grid, index, servers)

    Layout.draw_connections(edges)
    Layout.draw_nodes()
    xml = Layout.save()

    send_app_id = task_send_to_server_app(xml)

    return {'send_app_id': send_app_id}