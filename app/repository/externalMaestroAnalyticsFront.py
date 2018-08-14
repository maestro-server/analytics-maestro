
from app.views import app
from app.libs.logger import logger
from .externalMaestro import ExternalMaestro
from app.libs.notifyError import notify_error
from .maestroRequest import MaestroRequest

class ExternalMaestroAnalyticsFront(ExternalMaestro):
    
    def __init__(self, owner_id):
        base = app.config['MAESTRO_ANALYTICS_FRONT_URI']
        super().__init__(base, owner_id)

    def request(self, path, query, verb='post'):
        path = "%s/%s" % (self._base, path)
        MaestroRqt = MaestroRequest().set_headers(self._headers)

        try:
            MaestroRqt.exec_request_data(path, query, verb)
            logger.debug("MaestroRequest External path - %", path)
        except Exception as error:
            self.error_handling(task='ExternalMaestro', owner_id=self._owner_id, msg=str(error))

        return MaestroRqt

    def error_handling(self, task, owner_id, msg):
        return notify_error(task, owner_id, msg)