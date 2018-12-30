
from app import celery
from app.libs.network.baseNetwork import BaseNetwork
from app.services.gridOrchestrator import GridOrchestrator
from .enrichment_apps import task_enrichment
from .network_info import task_info_bussiness
from .notification import task_notification
from app.tasks.ws import task_ws


@celery.task(name="network.bussiness")
def task_network_bussiness(owner_id, graph_id, data, entries):

    try:
        network = BaseNetwork()
        network.make(data).get_graph()

        Orchestration = GridOrchestrator(network.graph)
        Orchestration.create(entries)

    except Exception as error:
        task_notification.delay(graph_id=graph_id, msg=str(error), status='error')
        task_ws.delay(graph_id, owner_id, "danger")
        raise error

    else:

        grid, index = Orchestration.get_mapping()
        edges = list(network.graph.edges(data='endpoint'))

        info = {
            'density': "{0:.2f}".format(network.get_density()),
            'ledges': len(edges)
        }

        enrichment_id = task_enrichment.delay(owner_id, graph_id, grid, index, edges)
        info_id = task_info_bussiness.delay(owner_id, graph_id, grid, index, info)

        return {'enrichment_id': str(enrichment_id), 'info_id': str(info_id), 'graph_id': graph_id, 'owner_id': owner_id}