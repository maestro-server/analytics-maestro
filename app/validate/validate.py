from flask_restful.reqparse import RequestParser


class Validate(object):
    def task_type(self, value):
        statuses = ["infra", "bussiness"]
        if value in statuses:
            return value

        raise ValueError()

    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("filters", type=str, default='{}')
        valid.add_argument("type", required=True, type=self.task_type, help="Use infra or bussiness")
        valid.add_argument("owner_user", type=str, required=True, help="Must've id owner")

        return valid.parse_args()
