import requests
from app import celery
from app.libs.url import FactoryDataURL
from app.tasks.notification import task_notification
from app.libs.statusCode import check_status
from app.libs.notifyError import notify_error

from app.services.root import Root


@celery.task(name="draw.infra", bind=True)
def task_draw_infra(self, owner_id, filters=''):
    path = FactoryDataURL.make(path="systems")
    context = requests.post(path, json={'query': filters})

    if context.status_code is 200:
        result = context.json()
        if 'found' in result and result['found'] > 0:
            return Root(result['items'])\
                                .validate_roots()\
                                .fill_gaps_root()\
                                .get_roots_id()

    if check_status(context):
        return notify_error(task='entry', owner_id=owner_id, msg=context.text)