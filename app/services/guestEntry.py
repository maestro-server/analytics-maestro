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

        print(cutover)
        for item in self._items:
            family = item.get('family')

            if family in self.hierarch[cutover:self.max]:
                print(key)

            print(self.hierarch[cutover-self.max:cutover])

        print()

        return []
    
    def multiple(self, n):
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
        return ['Serverless', 
    'ObjectStorage', 'ServiceDiscovery', 'VPN', 'CI/CD',  'Monitor', 'Cache', 'CDN', 'ApiGateway', 'Loadbalance', 'NAS', 'Logs', 'SMTP', 
    'Auth', 'Broker', 'Repository', 'Database', 'ContainerOrchestration', 'Application', 'ServiceMesh', 'DNS']

        return ['CDN', 'ApiGateway', 'Loadbalance', 'NAS', 'Application', 'Serverless', 
    'ObjectStorage', 'ServiceDiscovery', 'VPN', 'CI/CD',  'Monitor', 'Cache', 'Logs', 'SMTP', 
    'Auth', 'Broker', 'Repository', 'Database', 'ContainerOrchestration', 'ServiceMesh', 'DNS']
    