
from collections import Counter
from app import celery
from .notification import task_notification
from .network_clients import task_clients_bussiness
from app.libs.histograms.grid import GridHistogram
from app.libs.helpers.reduceDict import ReduceDict

def reduceServersinfo(fml):
    if isinstance(fml, list):
        return len(fml)

    return 0

@celery.task(name="info.bussiness")
def task_info_bussiness(owner_id, graph_id, grid, index, info):

    rSystem = ReduceDict()
    families = []
    servers = 0

    for current in index.values():
        fm = current[3].get('system')
        rSystem.push(fm)

        fml = current[3].get('family')
        families.append(fml)

        fml = current[3].get('servers')
        servers += reduceServersinfo(fml)


    families = dict(Counter(families))
    hist = GridHistogram(index).get_counter()
    systems = rSystem.get_bags()


    data = {
        'info': {
            'histograms': hist,
            'density': info.get('density'),
            'conections': info.get('ledges')
        },
        'isystems': {
            'items': systems,
            'total': len(rSystem)
        },
        'ifamilies': {
            'items': families,
            'total': len(index)
        },
        'iservers': {
            'total': servers
        }
    }

    not_id = task_notification.delay(graph_id=graph_id, msg=None, more=data)
    if systems:
        task_clients_bussiness.delay(owner_id, graph_id, systems)

    return {'not_id': str(not_id), 'graph_id': graph_id, 'owner_id': owner_id}