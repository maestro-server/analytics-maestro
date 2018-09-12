
from ..helperDraw import HelperDraw
from .drawPointerConnector import HelperPointerNodeConnector
from .drawNodeConnector import HelperNodeConnector


class HelperDrawConnector(HelperDraw):
    def __init__(self, size, off, matrix3d=None, HPointer=HelperPointerNodeConnector):
        super().__init__(size, matrix3d)

        self._off = off

        self._nodes = []
        self._hconnector = None
        self._hpointer = HPointer(matrix3d)

    def connect(self, node1, node2, HNodeConnector=HelperNodeConnector):

        self._hconnector = HNodeConnector(node1, node2)

        fpos = self._hconnector.do_first_node()
        fsize = self._hconnector.get_first_size()
        spos = self._hconnector.do_second_node()
        ssize = self._hconnector.get_second_size()

        diffs = self._hconnector.get_diffs()

        self._hpointer.node_mid_front(fpos, fsize)

        if self._hconnector.is_down():
            self.first_step(fpos, spos, fsize, ssize, diffs)

        if self._hconnector.is_double_down():
            self.second_step(fpos, diffs)

        if self._hconnector.is_up():
            self.revert_step(fpos, fsize, diffs)

        self._hpointer.point_mid_back(spos, ssize)
        self._hpointer.node_mid_back(spos, ssize)

        return self._hpointer.get_path()

    def first_step(self, fpos, spos, fsize, ssize, diffs):
        if fsize > 1 or diffs[0] == 0:
            self.ajust_corner(fpos, spos, fsize, ssize)
        else:
            self._hpointer.point_mid_front(fpos, fsize)

    def second_step(self, fpos, diffs):
        cx = fpos[0] + 1
        cy = fpos[1]

        if (cx in self._matrix3d._grid) and (cy in self._matrix3d._grid[cx]):
            check = self._matrix3d._grid[cx][cy][0]

            if check == '-':
                self._hpointer.point_mid_front(fpos, 1)
                self._hpointer.node_mid_front((fpos[0] + diffs[0], fpos[1]), 1)

            if check != '-':
                m = self.sizes(10, 40)

                self._hpointer.point_start_front(fpos, 1, m)
                self._hpointer.node_start_front((fpos[0] + diffs[0], fpos[1]), 1, m)

    def revert_step(self, fpos, fsize, diffs):
        m = self.sizes(12, 40)

        if diffs[1] <= 0:
            self._hpointer.point_start_front(fpos, 1)
        else:
            self._hpointer.point_end_front(fpos, fsize)

        self._hpointer.point_start_front((fpos[0], fpos[1] + diffs[1]), 1, m)
        self._hpointer.point_start_front((fpos[0] + diffs[0], fpos[1] + diffs[1]), 1, m)

    def ajust_corner(self, fpos, spos, fsize, ssize):
        _, y1 = self._matrix3d.rotateXY(fpos, fsize)()
        _, y2 = self._matrix3d.rotateXY(spos, ssize)()

        dy = y2 - y1

        cal = (self._size[1] * self._off[1]) / 5
        cal2 = cal / 2

        if dy >= -cal2:
            self._hpointer.point_end_front(fpos, fsize)
            return

        if dy <= -cal:
            self._hpointer.point_start_front(fpos, fsize)
            return

    def sizes(self, dx=1, dy=1):
        sx = self._size[0] * self._off[0]
        sy = self._size[1] * self._off[1]

        return (sx / dx, sy / dy)
