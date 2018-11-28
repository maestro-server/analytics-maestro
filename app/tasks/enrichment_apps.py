
from app import celery
from .draw_bussiness import task_draw_bussiness
from app.libs.transformDict import enrichment_apps_servers
from app.repository.externalMaestroOwneredData import ExternalMaestroOwneredData


@celery.task(name="enrichment.apps")
def task_enrichment(owner_id, graph_id, grid, index, edges):

    app_ids = list(index.keys())
    query = {"applications._id": app_ids}

    result = ExternalMaestroOwneredData(graph_id, owner_id)\
                    .list_request(path="servers", query=query)\
                    .get_results('items')

    enrichment_apps_servers(index, result)
    draw_id = task_draw_bussiness.delay(owner_id, graph_id, grid, index, edges)

    return {'draw_id': str(draw_id), 'graph_id': graph_id, 'owner_id': owner_id}