
from app import celery
from app.services.infra_network import InfraNetwork


@celery.task(name="network.bussiness", bind=True)
def task_network_infra(self, owner_id, data):
    pass

    return {'cardials': pos}