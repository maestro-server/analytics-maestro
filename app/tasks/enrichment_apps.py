
from app import celery
from .draw_bussiness import task_draw_bussiness
from app.repository.externalMaestroData import ExternalMaestroData


@celery.task(name="enrichment.apps")
def task_enrichment(owner_id, grid, index, edges):
    ids = index.keys()
    query = {"_id": list(ids)}

    ExternalRequest = ExternalMaestroData(owner_id=owner_id)
    items = ExternalRequest.get_request(path="servers", query=query)

    print(items)
    task_draw_bussiness(owner_id, grid, index, edges)

    return {'cardials': ""}