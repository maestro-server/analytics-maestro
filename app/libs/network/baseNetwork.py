import networkx as nx


class BaseNetwork(object):
    def __init__(self, G=nx.DiGraph):
        self.graph = G()
        self.clear_duplicate()

    def create_edge(self, item):
        if 'deps' in item:
            for dps in item['deps']:
                w = item.get('steps', -1)
                endpoint = dps.get('endpoint')
                self.graph.add_edge(item['_id'], dps['_id'], weight=w+1, endpoint=endpoint)

    def create_node(self, node_id, item, root = False):
        if node_id not in self.duplicate:
            self.graph.add_node(str(node_id), uid=item.get('_id'), root=root, attr=item)
            self.duplicate.append(node_id)

    def make(self, data, i=0):
        for item in data:
            self.create_node(item['_id'], item, i is 0)

            if 'nodes' in item and len(item['nodes']) > 0:
                self.make(item['nodes'], i + 1)

            self.create_edge(item)

        self.clear_duplicate()
        return self

    def get_graph(self):
        return self.graph

    def get_density(self):
        return nx.density(self.graph)

    def clear_duplicate(self):
        self.duplicate = []
