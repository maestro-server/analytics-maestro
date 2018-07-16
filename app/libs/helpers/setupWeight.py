

class HelperSetupWeight(object):
    def __init__(self, G):
        super().__init__()
        self._graph = G

    def find_weight(self, item, weight=0):
        pred = self._graph.in_edges(item, data=True)

        if pred and len(list(pred)) > 0:
            weight = max([it[2].get('weight') for it in pred]) + 1

        return weight

    def setup(self):
        nodes = self._graph.nodes()

        for node in nodes:
            w = self.find_weight(node)
            self._graph.nodes[node]['weight'] = w