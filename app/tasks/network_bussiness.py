
from app import celery
from app.libs.network.baseNetwork import BaseNetwork
from app.services.gridOrchestrator import GridOrchestrator
from .draw_bussiness import task_draw_bussiness


@celery.task(name="network.bussiness")
def task_network_bussiness(owner_id, data, entries):
    
    network = BaseNetwork()
    network.make(data).get_graph()

    Orchestration = GridOrchestrator(network.graph)
    Orchestration.create(entries)

    grid = Orchestration.get_grid().get_grid()
    index = Orchestration.get_grid()._index
    edges = network.graph.edges()

    task_draw_bussiness(owner_id, grid, index, edges)

    return {'cardials': ""}