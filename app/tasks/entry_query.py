
from app import celery
from app.services.root import Root
from app.repository.externalMaestroData import ExternalMaestroData


@celery.task(name="entry.api", bind=True)
def task_entry(self, owner_id, filters=''):

    ExternalRequest = ExternalMaestroData(owner_id=owner_id)
    items = ExternalRequest.get_request(path="systems", json={'query': filters})

    return Root(items, owner_id)\
                .validate_roots()\
                .fill_gaps_root(ExternalRequest)\
                .get_roots_id()