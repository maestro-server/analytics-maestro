
from .crawler import Crawler
from app.libs.logger import logger
from app.libs.notifyError import notify_error
from app.error.clientMaestroError import ClientMaestroError


class Root(object):

    def __init__(self, data, owner_id, crawler=Crawler):
        if not isinstance(data, (list, tuple)) or len(data) <= 0:
            err = ClientMaestroError("Dont exist any system (empty list)")
            notify_error('Entry', owner_id, err, "warning")
            raise err

        self.__data = data
        self.__owner_id = owner_id
        self.__bag_fallen = []
        self.__bag_apps = []

        self.crawler = crawler

    def push_bag(self, ids):
        self.__bag_apps = list(set(self.__bag_apps + ids))

    def validate_roots(self):
        for system in self.__data:
            entry = system.get('entry')
            if isinstance(entry, (list, tuple)) and len(entry) > 0:
                ids = self.map_reduce(entry)
                self.push_bag(ids)

            else:
                self.__bag_fallen.append(system.get('_id'))

        return self
    
    def fill_gaps_root(self, requester):

        if len(self.__bag_fallen) > 0:
            entries = self.crawler(self.__bag_fallen, requester)\
                            .find_apps()\
                            .get_entries()

            entries = self.map_reduce(entries)
            self.push_bag(entries)

        return self

    def get_roots_id(self):
        return self.__bag_apps

    def map_reduce(self, entry):
        return list(map(lambda x: x.get('_id'), entry))

    def cleanup(self):
        self.__data = []
        self.__system = []
        self.__entries = []