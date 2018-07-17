

def transform_dict(obj):
        trans = {}

        for item in obj:
            k = item.get('_id')
            trans[k] = item
        
        return trans

def append_servers(base, current):
    server = current[3].get('servers')
    if server:
        base += server
    return base