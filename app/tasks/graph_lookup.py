import json
from app import celery
from app.repository.externalMaestroData import ExternalMaestroData

from .network_infra import task_network_infra

types = {
    'infra': task_network_infra
}

@celery.task(name="graphlookup.api", bind=True)
def task_graphlookup(self, owner_id, entries, type):
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
                'maxDepth': 10,
                'depthField': 'steps'
            }
        },
        {'$project': {'name': 1, 'deps': 1, 'nodes.name': 1, 'nodes.steps': 1, 'nodes.deps': 1}}
    ];

    jpipeline = json.dumps(pipeline)
    ExternalRequest = ExternalMaestroData(owner_id=owner_id)
    items = ExternalRequest.get_request(path="aggregate", json={'entity': entity, 'pipeline': jpipeline})

    network_id = types[type](owner_id, items)

    return {'qtd': len(items)}