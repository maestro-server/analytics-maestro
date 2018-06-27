
from .crawler import Crawler


class Root(object):

    def __init__(self, data, crawler=Crawler):
        self.__data = data
        self.__bag_fallen = []
        self.__bag_apps = []

        self.crawler = crawler

    def push_bag(self, ids):
        self.__bag_apps = list(set(self.__bag_apps + ids))

    def validate_roots(self):
        for system in self.__data:
            entry = system.get('entry')

            if isinstance(entry, (list, tuple)) and len(entry) > 0:
                ids = list(map(lambda x: x.get('_id'), entry))
                self.push_bag(ids)

            else:
                self.__bag_fallen.append(system.get('_id'))

        return self
    
    def fill_gaps_root(self):
        entries = self.crawler(self.__bag_fallen)\
                        .find_apps()\
                        .propagate_entries()\
                        .get_entries()

        self.push_bag(entries)
        return self

    def get_roots_id(self):
        return self.__bag_apps

    def cleanup(self):
        self.__data = []
        self.__system = []
        self.__entries = []