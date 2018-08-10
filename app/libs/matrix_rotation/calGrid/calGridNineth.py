
from .calGrid import CalGrid


class CalGridNineth(CalGrid):
    def __init__(self, size, gsize=3):
        super().__init__(size, gsize)

    def build_map(self):
        if self._map == None:
            xbase, ybase = [self._base[x] for x in range(2)]
            cato_box, cato_node = self._cato

            yspace = self._size[1] - self._nsize[1]

            grid_x = (
                xbase * 2, xbase * 3, xbase * 4,
                xbase, xbase * 2, xbase * 3,
                0, xbase, xbase * 2
            )

            grid_y = (
                yspace - cato_box - cato_box,
                yspace - cato_box + cato_node - cato_box,
                yspace - cato_box,

                yspace - cato_box + cato_node - cato_box,
                yspace - cato_box,
                yspace - cato_box + cato_node,

                yspace - cato_box,
                yspace - cato_box + cato_node,
                yspace
            )

            self._map = grid_x, grid_y

        return self._map