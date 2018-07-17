
from app import celery
from app.services.root import Root
from app.repository.externalMaestroData import ExternalMaestroData

from .graph_lookup import task_graphlookup


@celery.task(name="entry.api")
def task_entry(owner_id, typed, filters={}):

    ExternalRequest = ExternalMaestroData(owner_id=owner_id)
    items = ExternalRequest.get_request(path="systems", query=filters)

    entries = Root(items, owner_id)\
                .validate_roots()\
                .fill_gaps_root(ExternalRequest)\
                .get_roots_id()

    task_graphlookup(owner_id, entries, typed)

    return {'entries': entries}