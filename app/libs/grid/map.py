from .swift import GridMapSwift
from .dummies import GridMapDummies
from .grid import Grid


class GridMap(Grid, GridMapSwift, GridMapDummies):

    def get_item_pos(self, item):
        if item in self._index:
            return self._index[item]

    def get_index(self, item=None):
        if item:
            return self._index.get(item)

        return self._index

    def is_node(self, x, y):
        mark = self.get_pos(x, y, self._dmark)
        return mark[0] != self._dmark

    def in_index(self, item):
        return item in self._index

    def create_position(self, pos, label, size=1, attr={}):
        self.create_index(label, pos, size, attr)
        return self._add_grid(*pos, label)

    def create_index(self, label, pos, size, attr):
        self._index[label] = (*pos, size, attr)
        return pos, size

    def inc_size_index(self, anode, qtd=1):
        tmp = self.get_index(anode)
        self.update_index(anode, (tmp[0], tmp[1]), tmp[2] + qtd, tmp[3])

    def update_index(self, anode, pos, size, attr):
        self.del_item(anode)
        self.create_index(anode, pos, size, attr)

    def del_item(self, anode):
        del self._index[anode]