
import requests
from app.error.clientMaestroError import ClientMaestroError

class MaestroRequest(object):
    
    def __init__(self):
        self.__context = None
        self.__headers = {}

    def exec_request(self, path, json, verb='post'):
        self.__context = getattr(requests, verb)(path, json=json, headers=self.__headers)
        return self

    def exec_request_data(self, path, xml, verb='post'):
        self.__context = getattr(requests, verb)(path, data=xml, headers=self.__headers)
        return self

    def set_headers(self, headers):
        self.__headers = headers
        return self

    def get_results(self):
        if self.__context.status_code is 200:
            result = self.__context.json()

            return result.get('items')

        raise ClientMaestroError(self.__context.text)
    
    def get_raw(self):
        return self.__context.text