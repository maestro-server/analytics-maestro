

class Crawler(object):

    def __init__(self, ids):
        self.__ids = ids
        self.__bag_ids = []

    def find_apps(self):
        return self

    def propagate_entries(self):
        return self

    def get_entries(self):
        return self.__bag_ids