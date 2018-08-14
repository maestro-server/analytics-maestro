
from app.libs.logger import logger
from flask_restful import Resource
from app.validate.validate import Validate

from app.tasks.graph_lookup import task_graphlookup
from app.tasks.entry_query import task_entry
from app.tasks.notification import task_notification
from app.libs.helpers.filterTransformation import FilterTransformation


class GraphApp(Resource):
    # @api {get} /graph/ Graph Bussiness
    # @apiName GetGraph
    # @apiGroup FGraph
    def post(self):

        valid = Validate().validate()

        if valid:
            owner_id = valid['owner_id']
            type = valid['type']
            graph_id = valid['_id']

            filterTrans = FilterTransformation()
            filters = filterTrans.transformation(valid)

            try:
                if filterTrans.is_("apps"):
                    entry_id = task_graphlookup(owner_id=owner_id, graph_id=graph_id, entries=filters, typed=type)
                else:
                    entry_id = task_entry(filters=filters, graph_id=graph_id, owner_id=owner_id, typed=type)

                return entry_id, 201

            except Exception as error:
                task_notification(owner_id=owner_id, msg=str(error), status='error')
                logger.error(error)
                return {'message': str(error)}, 501

            msg="Graph Bussiness [Entry] - Process - %s" % entry_id
            task_notification(owner_id=owner_id, msg=msg)

        return valid, 502