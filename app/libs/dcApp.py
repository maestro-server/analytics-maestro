class DcApps(object):
    allowed = ['aws', 'openstack', 'azure']

    @staticmethod
    def byServer(server, dft='premise'):

        if 'datacenters' in server:
            dc = server.get('datacenters')

            if 'provider' in dc:
                provider = dc.get('provider').lower()

                if provider in DcApps.allowed:
                    return provider

        return dft