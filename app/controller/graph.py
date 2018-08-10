
from app.libs.logger import logger
from flask_restful import Resource
from app.validate.validate import Validate

from app.tasks.entry_query import task_entry
from app.tasks.notification import task_notification


class GraphApp(Resource):
    # @api {get} /graph/ Graph Bussiness
    # @apiName GetGraph
    # @apiGroup FGraph
    def get(self):
        valid = Validate().validate()

        if valid:
            owner_id=valid['owner_id']
            type = valid['type']

            entry_id = task_entry(filters=valid['filters'], owner_id=owner_id, typed=type)
            try:
                entry_id = task_entry(filters=valid['filters'], owner_id=owner_id, typed=type)
            except Exception as error:
                task_notification(owner_id=owner_id, msg=str(error), status='error')
                logger.error(error)
                return {'message': str(error)}, 501

            msg="Graph Bussiness [Entry] - Process - %s" % entry_id
            task_notification(owner_id=owner_id, msg=msg)

        return valid, 502