
from app.libs.logger import logger
from .maestroRequest import MaestroRequest

class ExternalMaestro(object):

    def __init__(self, base, owner_id=None):
        self._base = base
        self._owner_id = owner_id

    def get_uri(self):
        self._base
        
    def get_request(self, path, json={}):
        return self.request(path, json).get_results()
    
    def put_request(self, path, json={}):
        return self.request(path, json, 'put').get_raw()
    
    def request(self, path, json, verb='post'):
        path = "%s/%s" % (self._base, path)
        MaestroRqt = MaestroRequest()

        try:
            MaestroRqt.exec_request(path, json, verb)
            logger.debug("MaestroRequest External path - %", path)
        except Exception as error:
            self.error_handling(task='ExternalMaestro', owner_id=self._owner_id, msg=str(error))

        return MaestroRqt

    def error_handling(self, task, owner_id, msg):
        logger.error("Analytics:  [%s] - %s", task, msg)