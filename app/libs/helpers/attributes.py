from .define import HelperDefineStep
from .succers import HelperDefineSuccersPredecessors


class HelperDefineAttributes(HelperDefineStep, HelperDefineSuccersPredecessors):
    def __init__(self, node, grid, G):
        self._graph = G
        self._node = node
        self._grid = grid

        self._direct_succers = []
        self._subdirect_succers = []
        self._predecessors = []

        self._succers_not_drawing = {'direct': [], 'subdirect': []}

        self._step = self.make_step()

    def get_id(self):
        return self.get_node_attr('label')