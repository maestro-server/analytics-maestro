
import requests
from app.libs.logger import logger
from app.error.clientMaestroError import ClientMaestroError

class MaestroRequest(object):
    
    def __init__(self, verb='get', headers={}):
        self.__context = None
        self.__headers = headers
        self.__path = None
        self.__verb = verb

    def exec_request(self, path, json=None, data=None):
        self.__context = getattr(requests, self.__verb)(path, json=json, data=data, headers=self.__headers)
        return self

    def get_status(self):
        try:
            return self.__context.status_code
        except Exception as error:
            raise ClientMaestroError("Endpoint not up %s" % self.__path)

    def get_json(self):
        logger.info("Request[CODE %s] - %s", self.get_status(), self.__path)

        if self.get_status() is 200:
            return self.__context.json()

        if self.get_status() in [500, 503, 504, 401, 403, 0]:
            raise ClientMaestroError(self.__context.text)