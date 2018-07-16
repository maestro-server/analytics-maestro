
from .histogram import Histogram


class GridHistogram(Histogram):
    def __init__(self, grid):
        super().__init__()
        self._grid = grid
        self.make()

    def make(self):
        clear = {}

        for key, value in self._grid.items():
            clear[key] = len(value)

        self.set_collections(clear)