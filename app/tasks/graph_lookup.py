import json
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
        {'$project': {'name': 1, 'deps': 1, 'nodes': 1}}
    ];

    jpipeline = json.dumps(pipeline)
    ExternalRequest = ExternalMaestroData(owner_id=owner_id)
    items = ExternalRequest.get_request(path="aggregate", json={'entity': entity, 'pipeline': jpipeline})
 
    network_id = types[typed](owner_id, items, entries)

    return {'qtd': len(items)}