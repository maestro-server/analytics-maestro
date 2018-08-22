class DcApps(object):
    allowed = ['aws', 'openstack', 'azure']

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