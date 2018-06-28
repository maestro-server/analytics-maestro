
import json

class Crawler(object):

    def __init__(self, ids, requester):
        self.__bag_systems = ids
        self.__bag_ids = []

        self._requester = requester

    def find_apps(self):
        systems = {
            'system._id': self.__bag_systems
        }
  
        filters = json.dumps(systems)
        items = self._requester.get_request(path="applications", json={'query': filters})
        
        print(items)
        return self

    def propagate_entries(self):
        return self

    def get_entries(self):
        return self.__bag_ids