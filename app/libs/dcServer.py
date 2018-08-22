
from app.libs.dcApp import DcApps


class DcServers(object):

    def __init__(self, servers=[]):
        self._servers = servers
        self.allowed = ['aws', 'openstack', 'azure']

    def byServer(self, app, servers=[], dft='premise'):

        if len(servers) > 0:
            return self.findDC(servers)

        if 'datacenters' in app:
            dc = app.get('datacenters')

            if 'provider' in dc:
                provider = dc.get('provider').lower()

                if provider in self.allowed:
                    return provider

        return dft


    def findDC(self, servers):
        dc = []

        for svs in servers:
            ss = self._servers.get(svs)
            itns = DcApps.byServer(ss)
            dc.append(itns)

        return ', '.join(dc)

