from svgwrite import Drawing
from .areaSVG import DrawArea
from .defsSVG import DefsSVG


class DrawTemplateSVG(object):
    def __init__(self, hist, nmax, darea=DrawArea, defs=DefsSVG):
        self._off = (40, 40)
        self._size = (20, 20)

        self._hist = hist
        self._nmax = nmax

        self._area = darea(self._off, self._size, hist, nmax).area()

        self.dwg = Drawing('test.svg', size=self._area)
        self._grid_defs = defs(self.dwg)

    def draw_app(self, pos, w, label):
        pos = self.cal_off(pos, w)
        self._grid_defs.app(pos, label, self._size)

    def draw_connect(self, pos1, pos2, w1, w2):
        pos1 = self.cal_pos_line(pos1, w1, self._size[0])
        pos2 = self.cal_pos_line(pos2, w2)

        self._grid_defs.line(pos1, pos2)

    def cal_off(self, pos, w):
        x = self.cal_offx(pos[0], w)
        y = self.cal_offy(pos[1], w)

        return (x, y)

    def cal_offy(self, y, w):
        off = 0
        # if self._hist[w] < self._nmax:
        #    off = (self._nmax - self._hist[w]) / 2
        #    off = off * (self._off[1] + self._size[1])

        return (y * self._off[1]) + (y * self._size[1]) + off

    def cal_offx(self, x, w):
        return (x * self._off[0]) + (x * self._size[0])

    def cal_pos_line(self, pos, w, suff_x=0):
        apos = self.cal_off(pos, w)
        y = apos[1] + (self._size[1] / 2)
        x = apos[0] + suff_x

        return (x, y)

    def save(self):
        self.dwg.save()
        return self.dwg.get_xml()