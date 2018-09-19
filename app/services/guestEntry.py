from functools import cmp_to_key


class GuestEntry(object):

    def __init__(self, items):
        self._entries = []
        self._items = items

        self.max = 3
        self.hierarch = GuestHierarchMap.map()

    def get_entries(self):
        self._items.sort(key=cmp_to_key(self.cmp_items))

        cutitem = self._items[0].get('family')
        idx = self.hierarch.index(cutitem) + 1
        cutover = self.multiple(idx)

        for key, item in enumerate(self._items):
            family = item.get('family')

            if family not in self.hierarch[cutover-self.max:cutover]:
                break

        self._items = self._items[:key-1]

        return self._items
    
    def multiple(self, n):
        if n % self.max is 0:
            return n

        return n + (self.max - n % self.max)

    def cmp_items(self, a, b):
        a1 = self.hierarch.index(a.get('family'))
        a2 = self.hierarch.index(b.get('family'))

        if a1 > a2:
            return 1
        elif a1 == a2:
            return 0
        else:
            return -1

class GuestHierarchMap(object):
    @staticmethod
    def map():
        return ['CDN', 'ApiGateway', 'Loadbalance', 'NAS', 'Application', 'Serverless', 
    'ObjectStorage', 'ServiceDiscovery', 'VPN', 'CI/CD',  'Monitor', 'Cache', 'Logs', 'SMTP', 
    'Auth', 'Broker', 'Repository', 'Database', 'ContainerOrchestration', 'ServiceMesh', 'DNS']
    