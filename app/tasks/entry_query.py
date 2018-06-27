import requests
import json
import os
from app import celery
from app.tasks.notification import task_notification
from app.libs.statusCode import check_status
from app.libs.notifyError import notify_error


@celery.task(name="entry.api", bind=True)
def task_entry(self, owner_id, filters={}):
    

    print(owner_id)

    if check_status(context):
        return notify_error(self.request.task, report_id, context.text)