
from app.libs.dcApp import DcApps


class DcServers(object):

    def __init__(self):
        self.allowed = ['aws', 'openstack', 'azure']

    def findDC(self, app, dft='premise'):
        servers = app.get('servers', [])
        dc = []

        if len(servers) > 0:
            for server in servers:
                itns = DcApps.byServer(server).capitalize()
                dc.append(itns)

            dc = set(dc)
            return ', '.join(dc)

        if 'datacenters' in app:
            dc = app.get('datacenters')

            if 'provider' in dc:
                provider = dc.get('provider').lower()

                if provider in self.allowed:
                    return provider

        return dft



