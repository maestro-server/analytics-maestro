
from app import celery

@celery.task(name="draw.infra", bind=True)
def task_draw_infra(self, owner_id, pos):
    pass
