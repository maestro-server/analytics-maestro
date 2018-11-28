
from .templateSVG import DrawTemplateSVG


class DrawLayout(object):
    def __init__(self, grid, index, draw=DrawTemplateSVG):

        self._grid = self.parser_json_grid(grid)
        self._index = index

        firstcol = min(self._grid, key=int)

        self._max_x = max(self._grid, key=int)
        self._max_y = max(self._grid[firstcol], key=int)
        self.setup_drawer(draw)

    def parser_json_grid(self, grid):
        output_dict = {}
        for key, value in grid.items():
            ikey = int(key)
            output_dict[ikey] = {}

            for k, v in value.items():
                ik = int(k)

                output_dict[ikey][ik] = v
        return output_dict


    def setup_drawer(self, draw):
        tmax = (self._max_x, self._max_y)
        self.drawer = draw(tmax, self._grid)

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