class HelperNodeConnector(object):
    def __init__(self, nd1, nd2):
        self._node = (nd1, nd2)
        self._diffs = None
        self._pos = []
        self._size = None

        self.setup()

    def setup(self):
        x1, y1, s1, _ = self._node[0]
        x2, y2, s2, _ = self._node[1]

        self._pos.append((x1, y1))
        self._pos.append((x2, y2))

        self._size = (s1, s2)

        self.diff_nodes()

    def diff_nodes(self):
        x1, y1 = self._pos[0]
        x2, y2 = self._pos[1]

        dx = x2 - x1
        dy = y2 - y1

        self._diffs = (dx - 1, dy)

    def get_diffs(self):
        return self._diffs

    def is_down(self):
        return self._diffs[0] >= 0

    def is_double_down(self):
        return self._diffs[0] >= 1

    def is_up(self):
        return self._diffs[0] < 0

    def do_first_node(self, x=0, y=0):
        return self._pos[0]

    def do_second_node(self, x=0, y=0):
        return self._pos[1]

    def get_first_size(self):
        return self._size[0]

    def get_second_size(self):
        return self._size[1]
