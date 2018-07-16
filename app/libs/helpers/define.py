class HelperDefineStep(object):
    def get_weight(self, node):
        dft = self._graph.nodes[node].get('weight')
        return self._get_weight(node, dft)

    def _get_weight(self, node, dft=0):
        if self._grid.in_index(node):
            idx = self._grid.get_index(node)
            return idx[0]

        return dft

    def get_node_attr(self, attr):
        return self._node.get(attr)

    def get_step(self):
        return self._step

    def make_step(self):
        node = self.get_id()

        if self._grid.in_index(node):
            idx = self._grid.get_index(node)
            return idx[0]

        return self.cal_step()

    def cal_step(self):
        predecessors = self.direct_predecessors()
        default_x = self.get_node_attr('weight')

        if len(predecessors) > 0:
            most = 0

            for pre in predecessors:
                wn = self._get_weight(pre)

                if most < wn:
                    most = wn

            default_x = most + 1
        return default_x