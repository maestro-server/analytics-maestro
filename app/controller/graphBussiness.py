import os
import json
from app import app
from flask_restful import Resource
from app.validate.validate import Validate

from app.tasks.entry_query import task_entry
from app.tasks.notification import task_notification


class GraphBussinessApp(Resource):
    # @api {get} /graph/bussiness Graph Bussiness
    # @apiName GetGraphBussiness
    # @apiGroup GBussiness
    def get(self):
        valid = Validate().validate()

        if valid:
            owner_id=valid['owner_user']

            try:
                entry_id = task_entry(filters=valid['filters'], owner_id=owner_id) 
            except Exception as error:
                task_notification(owner_id=owner_id, msg=str(error), status='error')
                return {'message': str(error)}, 501

            msg="Graph [Entry] - Process - %s" % entry_id
            return task_notification(owner_id=owner_id, msg=msg)

        return valid, 502