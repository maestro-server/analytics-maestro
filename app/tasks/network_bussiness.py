
from app import celery
from app.libs.network.baseNetwork import BaseNetwork
from app.services.gridOrchestrator import GridOrchestrator
from .enrichment_apps import task_enrichment


@celery.task(name="network.bussiness")
def task_network_bussiness(owner_id, data, entries):
    
    network = BaseNetwork()
    network.make(data).get_graph()

    Orchestration = GridOrchestrator(network.graph)
    Orchestration.create(entries)

    grid = Orchestration.get_grid().get_grid()
    index = Orchestration.get_grid().get_index()
    edges = network.graph.edges(data='endpoint')

    task_enrichment(owner_id, grid, index, edges)

    return {'cardials': ""}