
from .cosine import CalCosine


class MatrixRotation(object):
    def __init__(self, max_x, size, off, grid={}):
        self._size = size
        self._off = off
        self._mx = (size[0] * off[0]) / 2
        self._cosi = CalCosine.cal(self._mx)
        self._grid = grid

        self._rect_y = ((max_x - 1) * self._cosi)

    def cal_offy(self, x, y):
        return self._rect_y + (y * self._cosi) - (x * self._cosi)

    def cal_offx(self, x, y):
        return (y * self._mx) + (x * self._mx)