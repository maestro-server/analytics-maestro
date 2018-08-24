
from app.libs.matrix_rotation.cosine import CalCosine


class CalGrid(object):
    def __init__(self, size, gsize=2):
        self._map = None

        self._gsize = gsize
        self._size = size

        self._nsize = self.node_size()
        self._base = self.cal_base()
        self._cato = self.cal_cosins()

    def node_size(self):
        prop = self._gsize
        return (self._size[0] / prop, self._size[1] / prop)

    def get_size(self):
        return self._gsize ** 2

    def get_gsize(self):
        return self._gsize

    def get_nsize(self):
        return self._nsize

    def cal_base(self):
        return [self._nsize[x] / 2 for x in range(2)]

    def cal_cosins(self):
        cata = self._size[0] / self._gsize
        cos1 = CalCosine.cal(cata)
        cos2 = CalCosine.cal(self._base[0])
        return cos1, cos2

    def get_position(self, pos):
        mapper = self.build_map()
        return [mapper[x][pos] for x in range(2)]