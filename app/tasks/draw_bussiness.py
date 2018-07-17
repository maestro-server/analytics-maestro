
from app import celery
from app.libs.drawing.layoutSVG import DrawLayout
from .send_server_app import task_send_to_server_app


@celery.task(name="draw.bussiness")
def task_draw_bussiness(owner_id, grid, index, edges, servers):

    Layout = DrawLayout(grid, index)
    Layout.draw_nodes()
    Layout.draw_connections(edges)
    xml = Layout.save()

    task_send_to_server_app(xml)

    return {'cardials': ""}