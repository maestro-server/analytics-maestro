
import os
from app.views import app
from .externalMaestro import ExternalMaestro
from app.libs.notifyError import notify_error

class ExternalMaestroData(ExternalMaestro):
    
    def __init__(self, owner_id, graph_id):
        base = app.config['MAESTRO_DATA_URI']
        super().__init__(base, owner_id, graph_id)

    def error_handling(self, task, owner_id, graph_id, msg):
        return notify_error(task, owner_id, graph_id, msg)