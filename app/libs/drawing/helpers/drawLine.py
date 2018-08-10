
from .helperDraw import HelperDraw


class HelperDrawLabel(HelperDraw):
    def label_by_node(self, pos, node, maxl=10):
        name = node.get('name', '-')

        name = name[0:maxl]
        ln = len(name)

        fsize = self._size[0] * 0.16
        sposy = self._size[1] * 1.18

        sposx = (self._size[1] * 0.65) + (ln * (fsize * 0.24))

        npos = [-1 * pos[x] for x in range(2)]
        npos = (npos[0] - sposx, npos[1] + sposy)

        degrees = (-30.404, 41.)

        mpos = (pos[0] + 15, pos[1])
        transf = (*mpos, *degrees, *npos)

        opts = {
            'font_size': fsize,
            'transform': 'translate(%s, %s) skewY(%s) skewX(%s) translate(%s, %s)' % transf}

        return name, pos, opts