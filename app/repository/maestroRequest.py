
import requests
from app.error.clientMaestroError import ClientMaestroError

class MaestroRequest(object):
    
    def __init__(self):
        self.__context = None

    def exec_request(self, path, json, verb='post'):
        self.__context = getattr(requests, verb)(path, json=json)
        return self
    
    def get_results(self):
        if self.__context.status_code is 200:
            result = self.__context.json()

            return result.get('items')

        raise ClientMaestroError(self.__context.text)
    
    def get_raw(self):
        return self.__context.text