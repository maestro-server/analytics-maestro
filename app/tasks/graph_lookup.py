
from app import celery
from app.repository.externalMaestroData import ExternalMaestroData

from .network_bussiness import task_network_bussiness

types = {
    'bussiness': task_network_bussiness
}

@celery.task(name="graphlookup.api")
def task_graphlookup(owner_id, entries, typed):
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
                    'name': 1, 
                    'family': 1,
                    'servers': 1,
                    'deps._id': 1, 
                    'deps.endpoint': 1, 
                    'nodes._id': 1, 
                    'nodes.deps': 1, 
                    'nodes.name': 1,
                    'nodes.steps': 1,
                    'nodes.family': 1,
                    'nodes.servers': 1,
                    'nodes.system': 1,
                    'nodes.datacenters': 1
                }
            }
    ];

    ExternalRequest = ExternalMaestroData(owner_id=owner_id)
    items = ExternalRequest.get_aggregation(path="aggregate", entity=entity, pipeline=pipeline)
    network_id = types[typed](owner_id, items, entries)

    return {'qtd': len(items)}