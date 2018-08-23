
from .histogram import Histogram


class GridHistogram(Histogram):
    def __init__(self, index):
        super().__init__()
        self._index = index
        self.make()

    def make(self):
        clear = {}

        for key, value in self._index.items():
            step = value[0]

            if step not in clear:
                clear[step] = 0

            clear[step] += 1

        self.set_collections(clear)