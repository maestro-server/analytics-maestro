import os
import json
from app import app
from flask_restful import Resource


class HomeApp(Resource):
    # @api {get} / Ping
    # @apiName GetPing
    # @apiGroup Ping

    # @apiSuccessExample {json} Success-Response:
    # HTTP/1.1 201 OK
    # {
    #    app: (String)
    #    description: (String)
    #    version: (String)
    # }
    def get(self):
        root_path = os.path.join(app.root_path, '..')

        file = open(root_path + '/package.json')
        json_data = file.read()
        data = json.loads(json_data)

        keys = ['name', 'description', 'version', 'license']
        return dict(zip(keys, [data[k] for k in keys]))
