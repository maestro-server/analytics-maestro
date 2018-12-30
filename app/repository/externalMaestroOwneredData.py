
import json
from app.views import app
from app.libs.logger import logger
from .externalMaestro import ExternalMaestro
from app.repository.libs.notifyError import notify_error
from app.services.privateAuth.decorators.external_private_token import add_external_header_auth

@add_external_header_auth
class ExternalMaestroOwneredData(ExternalMaestro):
    
    def __init__(self, entity_id=None, owner_id=None):
        base = app.config['MAESTRO_DATA_URI']
        self._owner_id = owner_id
        self.ent_id = entity_id

        super().__init__(base)
        self.private_auth_header()

    def list_request(self, path, query={}, active=True):
        merged = self.make_filter(query, active)
        mquery = json.dumps(merged)

        self._results = self.request(path, {'query': mquery}, 'post')
        return self

    def make_filter(self, filter, active=True):
        base = {'roles._id': self._owner_id, 'active': active}

        if any(filter) and isinstance(filter, dict):
            return {**base, **filter}

        return base

    def error_handling(self, task, msg):

        if self.ent_id:
            return notify_error(task=task, msg=msg, graph_id=self.ent_id)

        logger.error("MaestroData:  [%s] - %s", task, msg)