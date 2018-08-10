
from .calGrid import CalGrid


class CalGridFourth(CalGrid):
    def __init__(self, size, gsize=2):
        super().__init__(size, gsize)

    def build_map(self):
        if self._map == None:
            xbase, ybase = [self._base[x] for x in range(2)]
            cato_box, cato_node = self._cato

            yspace = (self._size[1] / self._gsize)

            grid_x = (xbase, xbase * 2, 0, xbase)
            grid_y = (
                yspace - cato_box,
                yspace - cato_box + cato_node,
                yspace - cato_box + cato_node,
                yspace
            )

            self._map = grid_x, grid_y

        return self._map