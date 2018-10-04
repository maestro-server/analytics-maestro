
import json
from app.views import app
from app.libs.logger import logger
from .externalMaestroData import ExternalMaestroData
from app.repository.libs.notifyError import notify_error

class ExternalMaestroOwneredData(ExternalMaestroData):
    
    def __init__(self, entity_id=None, owner_id=None):
        self._owner_id = owner_id
        super().__init__(entity_id)

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