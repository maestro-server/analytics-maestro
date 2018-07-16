
from .histogram import Histogram


class GraphHistogram(Histogram):
    def __init__(self, G):
        super().__init__()
        self._graph = G
        self.make()

    def find_weight(self, item):
        weight = self._graph.nodes[item].get('weight')

        if not weight:
            pred = self._graph.in_edges(item, data=True)

            if pred and len(list(pred)) > 0:
                weight = max([it[2].get('weight') for it in pred]) + 1

        return weight

    def make(self):
        nodes = self._graph.nodes()
        weights = []

        for node in nodes:
            w = self.find_weight(node)
            weights.append(w)

        self.set_collections(weights)