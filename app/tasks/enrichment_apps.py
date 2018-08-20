
from functools import reduce
from app import celery
from .draw_bussiness import task_draw_bussiness
from app.libs.transformDict import append_servers, transform_dict
from app.repository.externalMaestroData import ExternalMaestroData



@celery.task(name="enrichment.apps")
def task_enrichment(owner_id, graph_id, grid, index, edges):
    
    servers_id = reduce(append_servers, index.values(), [])
    servers_id = list(set(servers_id)) #remove duplicate
    query = {"_id": servers_id}

    ExternalRequest = ExternalMaestroData(owner_id=owner_id, graph_id=graph_id)
    result = ExternalRequest.get_request(path="servers", query=query)

    servers = transform_dict(result)
    
    draw_id = task_draw_bussiness.delay(owner_id, graph_id, grid, index, edges, servers)

    return {'draw_id': str(draw_id), 'graph_id': graph_id, 'owner_id': owner_id}



