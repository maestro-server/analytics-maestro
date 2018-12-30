
from app.tasks.notification import task_notification


def notify_error(task, graph_id, msg, status="error"):
    msg = '[%s] %s' % (task, msg)
    notification_id = task_notification(graph_id=graph_id, msg=msg, status=status)
    return {'name': task, 'notification-id': str(notification_id)}