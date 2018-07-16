class Grid(object):
    def __init__(self):
        self.clean()
        self._dmark = '-'

    def get_grid(self):
        return self._grid

    def has_pos(self, x, y):
        return (x in self._grid) and (y in self._grid[x])

    def get_pos(self, x, y, deft=None):
        if self.has_pos(x, y):
            return self._grid[x][y]

        return deft

    def in_grid(self, step):
        return step in self._grid

    def not_in_grid(self, step):
        return step not in self._grid

    def max_y(self, step):
        return max(self._grid[step], key=int)

    def max_x(self):
        return max(self._grid, key=int)

    def _add_grid(self, x, y, item):
        if x not in self._grid:
            self._grid[x] = {}

        self._grid[x][y] = item
        return (x, y)

    def del_grid(self, columm, line):
        del self._grid[columm][line]

    def clean(self):
        self._grid = {}
        self._index = {}