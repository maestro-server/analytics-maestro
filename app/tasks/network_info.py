
from collections import Counter
from app import celery
from app.libs.transformDict import append_servers
from app.libs.histograms.grid import GridHistogram
from .notification import task_notification

class ReduceSystem(object):

    def __init__(self):
        self._isystem = []
        self._bags = []

    def push(self, sys):

        if (sys is not None) and isinstance(sys, list):
            for item in sys:
                _id = item.get('_id')
                if _id not in self._isystem:
                    self._isystem.append(_id)
                    self._bags.append(item)

    def get_bags(self):
        return self._bags

    def __len__(self):
        return len(self.get_bags())


def reduceServersinfo(fml):
    if isinstance(fml, list):
        return len(fml)

    return 0


@celery.task(name="info.bussiness")
def task_info_bussiness(owner_id, graph_id, grid, index, info):

    rSystem = ReduceSystem()
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
    hist = GridHistogram(grid).get_counter()

    data = {
        'info': {
            'systems': rSystem.get_bags(),
            'families': families,
            'histograms': hist,
            'density': info.get('density')
        },
        'counters': {
            'systems': len(rSystem),
            'servers': servers,
            'apps': len(index),
            'conection': info.get('ledges')
        }
    }

    not_id = task_notification.delay(graph_id=graph_id, owner_id=owner_id, msg=None, more=data)

    return {'not_id': str(not_id), 'graph_id': graph_id, 'owner_id': owner_id}