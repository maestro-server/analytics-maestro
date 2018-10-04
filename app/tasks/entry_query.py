
from app import celery
from app.services.root import Root
from app.repository.externalMaestroOwneredData import ExternalMaestroOwneredData

from .graph_lookup import task_graphlookup


@celery.task(name="entry.api")
def task_entry(owner_id, graph_id, typed, filters={}):

    items = ExternalMaestroOwneredData(graph_id, owner_id)\
                    .list_request(path="systems", query=filters)\
                    .get_results('items')

    entries = Root(items, owner_id)\
                .validate_roots()\
                .fill_gaps_root(ExternalMaestroOwneredData)\
                .get_roots_id()

    lookup_id = None
    if len(entries) > 0:
        lookup_id = task_graphlookup.delay(owner_id, graph_id, entries, typed)

    return {'entries': entries, 'graph_id': graph_id, 'owner_id': owner_id, 'lookup_id': lookup_id}