from flask_restful.reqparse import RequestParser


class Validate(object):
    def task_type(self, value):
        statuses = ["infra", "bussiness"]
        if value in statuses:
            return value

        raise ValueError()

    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("clients", type=dict, action='append')
        valid.add_argument("systems", type=dict, action='append')
        valid.add_argument("apps", type=dict, action='append')
        valid.add_argument("type", required=True, type=self.task_type, help="Use infra or bussiness")
        valid.add_argument("owner_id", type=str, required=True, help="Must've owner id")
        valid.add_argument("_id", type=str, required=True, help="Must've graph id")

        return valid.parse_args()
