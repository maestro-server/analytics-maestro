from app.libs.statusCode import string_status
from app.tasks.notification import task_notification


def notify_error(task, report_id, msg):
    notification_id = task_notification.delay(report_id=report_id, msg=msg, status='error')
    return string_status(task, notification_id)