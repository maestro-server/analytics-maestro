

def enrichment_apps_servers(mapper, servers):

    for server in servers:
        apps = server.get('applications')

        dserver = {k: server.get(k, None) for k in (
            'hostname', 'ipv4_private', 'ipv4_public', 'datacenters', 'services', 'storage', 'cpu', 'memory',
            'environment', 'role', 'os')}

        append_apps(mapper, apps, dserver)


def append_apps(mapper, apps, server):

    for app in apps:
        app_id = app.get('_id')

        if app_id in mapper:
            servers = mapper[app_id][3].get('servers', [])
            servers.append(server)

            mapper[app_id][3]['servers'] = servers