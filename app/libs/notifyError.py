from app.libs.statusCode import string_status
from app.tasks.notification import task_notification


def notify_error(task, owner_id, msg):
    msg = '[%s] %s' % (task, msg)
    notification_id = task_notification(owner_id=owner_id, msg=msg, status='error')
    return string_status(task, notification_id)