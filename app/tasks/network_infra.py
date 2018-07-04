
from app import celery
from app.services.infra_network import InfraNetwork


@celery.task(name="network.infra", bind=True)
def task_network_infra(self, owner_id, data):
    options = {
        'with_labels': False,
        'arrowsize': 15,
        'node_shape': 's',
        'node_size': 500,
        'node_color': '#782675',
        'font_color': 'white',
        'alpha': 0.9,
        'linewidths': 5
    }

    labels = {
        'font_weight': 'bold'
    }

    network = InfraNetwork()
    network.make(data).get_graph()
    pos = network.save_svg(options, labels)

    return {'cardials': pos}