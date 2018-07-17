
import json
from app.services.guestEntry import GuestEntry

class Crawler(object):

    def __init__(self, ids, requester, guest=GuestEntry):
        self.__bag_systems = ids
        self.__bag_ids = []

        self.__guest = guest
        self._requester = requester

    def find_apps(self):
        systems = {
            'system._id': self.__bag_systems
        }

        items = self._requester.get_request(path="applications", query=systems)

        if isinstance(items, (list, tuple)) and len(items) > 0:
            self.__bag_ids = self.__guest(items).get_entries()

        return self

    def get_entries(self):
        return self.__bag_ids