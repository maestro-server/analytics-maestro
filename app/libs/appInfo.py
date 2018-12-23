
import os
import json
from app import app


def appInfo():
    root_path = os.path.join(app.root_path, '..')

    file = open(root_path + '/package.json')
    json_data = file.read()
    data = json.loads(json_data)

    keys = ['name', 'description', 'version', 'license']
    return dict(zip(keys, [data[k] for k in keys]))