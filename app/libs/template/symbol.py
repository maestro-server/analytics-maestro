

from svgwrite import Drawing
from .manageStyle import ManageStyle


class Symbol(object):
    def __init__(self, draw=Drawing, mstyle=ManageStyle):
        self.dwg = draw
        self._s_basket = {}
        self._proportion = {}

        self._factor_proportion = 10

        self._manager_style = mstyle(self.dwg)

    def create_symbol(self, name, objs, viewbox):
        symbol = self.dwg.symbol(id=name)
        self.dwg.defs.add(symbol)

        symbol.viewbox(*viewbox)
        symbol.fit(vert='bottom')

        for obj in objs:
            symbol.add(obj)

        self._s_basket[name] = symbol

    def create_marker(self, name, objs, viewbox, opts):
        symbol = self.dwg.marker(id=name, **opts)
        self.dwg.defs.add(symbol)

        symbol.viewbox(*viewbox)

        for obj in objs:
            symbol.add(obj)

        self._s_basket[name] = symbol

    def create_group(self, name):
        g = self.dwg.defs.add(self.dwg.g(id=name))
        return g

    def get_symbol(self, name):
        return self._s_basket[name]

    def use_symbol(self, name, pos, opts={}):
        syb = self.get_symbol(name)
        return self.dwg.use(syb, insert=pos, **opts)

    def get_proportion(self, k):
        return self._proportion[k]

    def set_proportion(self, k, val):
        x = val[0] / self._factor_proportion
        y = val[1] / self._factor_proportion
        self._proportion[k] = (x, y)

    def square(self, pos, size, opts={}):
        return self.dwg.rect(insert=pos, size=size, **opts)

    def polyline(self, points, opts={}):
        return self.dwg.polyline(points=points, **opts)

    def text(self, title, pos, opt={}):
        return self.dwg.text(title, insert=pos, **opt)

    def multiline(self, ltxt, pos, opts={}):
        if not isinstance(ltxt, list):
            raise Exception("Need to be a list")

        atext = self.text("", pos)
        for opts in ltxt:
            label = opts.get('text')
            del opts['text']
            atext.add(self.tspan(label, opts))

        return atext

    def tspan(self, text, opts={}):
        return self.dwg.tspan(text, **opts)

    def line(self, pos, opts={}):
        cx, cy = pos
        return self.dwg.line(start=cx, end=cy, **opts)

    def path(self, d, opts):
        return self.dwg.path(d, **opts)

    def conn(self, d):
        opts = {
            'stroke_width': "1",
            'stroke': "black",
            'fill': "none",
            'opacity': 0.8,
            "marker_end": self.get_symbol('markers.arrow').get_funciri(),
            'class_': 'conector'
        }

        return self.path(d, opts)

    def conn_holder(self, d):
        opts = {
            'stroke_width': 18,
            'stroke': "black",
            'fill': "none",
            'opacity': 0,
            'class_': 'conector_h'
        }

        return self.path(d, opts)

    def brightness(self, idd="brightness", force=0.6):
        flt = self.dwg.filter(id=idd)
        dflt = self.dwg.defs.add(flt)

        feComp = dflt.feComponentTransfer()
        feComp.feFuncR('linear', slope=force)
        feComp.feFuncG('linear', slope=force)
        feComp.feFuncB('linear', slope=force)
        return flt