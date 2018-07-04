import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

class InfraNetwork(object):
    def __init__(self, G=nx.DiGraph):
        self.graph = G()

    def create_edge(self, parent, item):
        if 'deps' in parent:
            for dps in parent['deps']:
                w = item.get('steps', 0)
                self.graph.add_edge(item['name'], dps['name'], weight=10 - w)

    def create_node(self, item):
        self.graph.add_node(item['name'], object=item)

    def make(self, data):
        for item in data:
            self.create_node(item)
            self.create_edge(item, item)

            for sub in item['nodes']:
                self.create_node(sub)
                self.create_edge(sub, sub)

        return self

    def get_graph(self):
        return self.graph

    def get_cardials(self):
        pos = graphviz_layout(self.graph, prog='circo')
        return pos

    def save_svg(self, options, labels):
        plt.figure(figsize=(8, 8))
        pos = self.get_cardials()

        nx.draw(self.graph, pos, **options)

        pos_higher = {}
        y_off = 9  # offset on the y axis
        x_off = 0

        for k, v in pos.items():
            pos_higher[k] = (v[0] - x_off, v[1] - y_off)

        nx.draw_networkx_labels(self.graph, pos=pos_higher, **labels)

        plt.savefig('twopi.svg')
        return pos
