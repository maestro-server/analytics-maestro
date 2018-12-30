
from app import celery
from app.repository.externalMaestroData import ExternalMaestroData
from .notification import task_notification
from .network_bussiness import task_network_bussiness
from app.tasks.ws import task_ws

types = {
    'bussiness': task_network_bussiness
}

@celery.task(name="graphlookup.api")
def task_graphlookup(owner_id, graph_id, entries, typed):
    entity = 'applications'

    pipeline = [
        {'$match': {'_id': {'$in': entries}, 'roles._id': owner_id}},
        {
            '$graphLookup': {
                'from': entity,
                'startWith': '$deps._id',
                'connectFromField': 'deps._id',
                'connectToField': '_id',
                'as': 'nodes',
                'maxDepth': 40,
                'depthField': 'steps'
            }
        },
        {
            '$project':
                {
                    '_id': 1,
                    'name': 1, 
                    'family': 1,
                    'environment': 1,
                    'cluster': 1,
                    'language': 1,
                    'servers': 1,
                    'system': 1,
                    'datacenters': 1,
                    'size': 1,
                    'deps._id': 1, 
                    'deps.endpoint': 1, 
                    'nodes._id': 1, 
                    'nodes.deps': 1, 
                    'nodes.name': 1,
                    'nodes.steps': 1,
                    'nodes.family': 1,
                    'nodes.environment': 1,
                    'nodes.cluster': 1,
                    'nodes.language': 1,
                    'nodes.servers': 1,
                    'nodes.system': 1,
                    'nodes.datacenters': 1,
                    'nodes.size': 1
                }
            }
    ];

    items = ExternalMaestroData(graph_id)\
                    .list_aggregation(path="aggregate", entity=entity, pipeline=pipeline)\
                    .get_results('items')

    if items:
        network_id = types[typed].delay(owner_id, graph_id, items, entries)
        return {'qtd': len(items), 'graph_id': graph_id, 'owner_id': owner_id, 'network_id': str(network_id)}

    else:
        task_notification.delay(graph_id=graph_id, msg="Empty dependencies", status="warning")
        task_ws.delay(graph_id, owner_id, "warning")
        return {'qtd': len(items)}

