
from app.libs.logger import logger
from flask_restful import Resource
from app.validate.validate import Validate

from app.tasks.graph_lookup import task_graphlookup
from app.tasks.entry_query import task_entry
from app.tasks.notification import task_notification
from app.libs.helpers.filterTransformation import FilterTransformation


class GraphApp(Resource):
    """
    @api {post} /graph/ Graph Bussiness
    @apiName GetGraph
    @apiGroup Graph

    @apiParam(Param) {String} owner_id Owner ID
    @apiParam(Param) {String} type Graph type [Bussiness]
    @apiParam(Param) {String} _id Graph id, need to be create by server app

    @apiPermission JWT (Read | Write | Admin)
    @apiHeader (Auth) {String} Authorization JWT {Token}

    @apiError (Error) PermissionError Token don`t have permission
    @apiError (Error) Unauthorized Invalid Token
    @apiError (Error) NotFound List is empty

    @apiSuccessExample {json} Success-Response:
            HTTP/1.1 201 OK
             {
             }
    """
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
                    entry_id = task_graphlookup.delay(owner_id=owner_id, graph_id=graph_id, entries=filters, typed=type)
                else:
                    entry_id = task_entry.delay(filters=filters, graph_id=graph_id, owner_id=owner_id, typed=type)

                logger.info(entry_id);
                return str(entry_id), 201

            except Exception as error:
                task_notification.delay(graph_id=graph_id, owner_id=owner_id, msg=str(error), status='error')
                logger.error(error)
                return {'message': str(error)}, 501

        return valid, 502