
from .templateSVG import DrawTemplateSVG


class DrawLayout(object):
    def __init__(self, grid, index, servers={}, draw=DrawTemplateSVG):

        self._grid = grid
        self._index = index

        firstcol = min(self._grid, key=int)

        self._max_x = max(self._grid, key=int)
        self._max_y = max(self._grid[firstcol], key=int)
        self.setup_drawer(draw, servers)

    def setup_drawer(self, draw, servers):
        tmax = (self._max_x, self._max_y)
        self.drawer = draw(tmax, servers, self._grid)

    def draw_nodes(self):
        for _, node in self._index.items():
            self.drawer.draw_app(node)

        return self

    def draw_connections(self, edges):
        for edge in edges:
            edg = [self._index[edge[x]] for x in range(2)]
            self.drawer.draw_connect(*edg, edge[2])

        return self

    def save(self):
        return self.drawer.save()