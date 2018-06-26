

def check_status(context):
    return context.status_code in [400, 403, 404, 500, 501, 502, 503]

def string_status(task, notification_id):
    return {'name': task, 'notification-id': str(notification_id)}

def notify_error(task, report_id, msg):
    notification_id = task_notification.delay(report_id=report_id, msg=msg, status='error')
    return string_status(task, notification_id)