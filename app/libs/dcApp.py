class DcApps(object):
    allowed = ['aws', 'openstack', 'azure', 'google cloudengine', 'digital ocean', 'linode', 'rackspace', 'heroku', 'ovh', 'godaddy']

    @staticmethod
    def byServer(server, dft='premise'):

        if isinstance(server, dict):
            dc = server.get('datacenters')
            if dc:
                provider = dc.get('provider')

                if provider:
                    provider = provider.lower()

                    if provider in DcApps.allowed:
                        return provider

        return dft

    @staticmethod
    def byApps(node, lservers):
        obj = node
        servers = node.get('servers', [])

        if len(servers) > 0:
            obj = lservers.get(servers[0])

        return DcApps.byServer(obj)


