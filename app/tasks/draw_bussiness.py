
from app import celery
from app.libs.drawing.layoutSVG import DrawLayout


@celery.task(name="draw.bussiness")
def task_draw_bussiness(owner_id, grid, index, edges, servers):

    Layout = DrawLayout(grid, index)
    Layout.draw_nodes()
    Layout.draw_connections(edges)
    Layout.save()

    return {'cardials': ""}