
from .calGrid import CalGrid


class CalGridZero(CalGrid):
    def __init__(self, size, gsize=1):
        super().__init__(size, gsize)

    def build_map(self):
        if self._map == None:
            grid_x = [0]
            grid_y = [0]

            self._map = grid_x, grid_y

        return self._map