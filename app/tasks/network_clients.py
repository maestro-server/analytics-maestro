
from app import celery
from .notification import task_notification
from app.libs.helpers.reduceDict import ReduceDict
from app.repository.externalMaestroOwneredData import ExternalMaestroOwneredData


@celery.task(name="clients.bussiness")
def task_clients_bussiness(owner_id, graph_id, systems):

    systems_id = list(map(lambda x: x.get('_id'), systems))
    query = {"_id": systems_id}

    result = ExternalMaestroOwneredData(graph_id, owner_id)\
                    .list_request(path="systems", query=query)\
                    .get_results('items')

    rClients = ReduceDict()

    for item in result:
        clt = item.get('clients')
        rClients.push(clt)


    data = {
        'iclients': {
            'items': rClients.get_bags(),
            'total': len(rClients)
        }
    }

    not_id = task_notification.delay(graph_id=graph_id, owner_id=owner_id, msg=None, more=data)

    return {'not_id': str(not_id), 'graph_id': graph_id, 'owner_id': owner_id}