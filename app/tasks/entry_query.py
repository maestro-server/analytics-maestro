
from app import celery
from app.services.root import Root
from app.repository.externalMaestroOwneredData import ExternalMaestroOwneredData
from .notification import task_notification
from .graph_lookup import task_graphlookup
from app.tasks.ws import task_ws


@celery.task(name="entry.api")
def task_entry(owner_id, graph_id, typed, filters={}):

    ItnMaestroData = ExternalMaestroOwneredData(graph_id, owner_id)
    items = ItnMaestroData\
            .list_request(path="systems", query=filters)\
            .get_results('items')

    entries = Root(items, owner_id, graph_id)\
                .validate_roots()\
                .fill_gaps_root(ItnMaestroData)\
                .get_roots_id()

    qtdl = len(entries)
    if qtdl > 0:
        lookup_id = task_graphlookup.delay(owner_id, graph_id, entries, typed)
        return {'qtd': qtdl, 'graph_id': graph_id, 'owner_id': owner_id, 'lookup_id': lookup_id}

    else:
        task_notification.delay(graph_id=graph_id, msg="Empty entry point", status="warning")
        task_ws.delay(graph_id, owner_id, "warning")
        return {'qtd': qtdl}