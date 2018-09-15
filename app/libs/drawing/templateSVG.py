

from svgwrite import Drawing
from .areaSVG import DrawArea
from .helpers.drawLabel import HelperDrawLabel
from .helpers.drawTooltips import HelperDrawTooltips
from .helpers.drawPolilyne import HelperDrawBasePolyline
from .helpers.drawApplications import HelperDrawApplication
from .helpers.connector.drawConnector import HelperDrawConnector
from app.libs.matrix_rotation.matrix3D import Matrix3D
from app.libs.template.symbolAssets import SymbolAssets


class DrawTemplateSVG(object):
    def __init__(self, tmax, servers, grid, darea=DrawArea, symbols=SymbolAssets, m3d=Matrix3D):
        self._off = (2.2, 2.5)
        size = 100
        self._size = (size, size * 1.9)

        self._matrix3d = m3d(tmax[0], self._size, self._off, grid)

        self._area = darea(self._off, self._size, tmax[0], tmax[1], grid).area()

        self.dwg = Drawing('graph.svg', size=self._area, id="graph")
        self.dwg.viewbox(0, 0, *self._area)
        self._symbols = symbols(self.dwg)
        self._servers = servers

        self.setup()

    def setup(self):
        self.setup_background()
        self.setup_brightness()
        self.setup_marker()

    def setup_background(self):
        symbol = self._symbols.square((0, 0), size=self._area, opts={'fill': "#eaeaea"})
        self.add(symbol)

    def setup_brightness(self):
        self._symbols.brightness()
        self._symbols.brightness("darker", 0.4)

    def setup_marker(self):
        s = self._size[0] / 8

        opts = {
            'insert': (152, 3),
            'size': (s, s)
        }

        self._symbols.asset_marker('markers.arrow', opts)

    def boundary_box(self, pos, node):
        opts = {
            'id': node.get('_id')
        }

        symbol = self._symbols.asset('boundaries_box.front', 'default boundaries', (pos[0], pos[1]), self._size, opts)
        self.add(symbol)

    def draw_label(self, pos, node):
        text = HelperDrawLabel(self._size, self._matrix3d) \
            .label_by_node(pos, node)

        symbol = self._symbols.text(*text)
        self.add(symbol)

    def draw_app(self, item):
        cad1 = [item[x] for x in range(2)]
        node = item[3]

        pos = self._matrix3d.rotateNodeXY(item)()

        self.draw_root(item)
        self.draw_grid_size(cad1, item[2])
        self.grid_box(pos)
        self.draw_execute(pos, node)
        self.boundary_box(pos, node)
        self.draw_label(pos, node)
        self.draw_tooltips(node)

    def draw_execute(self, pos, node):
        hDrawApp = HelperDrawApplication(self._size, self._servers)
        hDrawApp.execute(pos, node)

        pSymb = hDrawApp.get_apps()

        for symb in pSymb:
            symbol = self._symbols.asset(*symb)
            self.add(symbol)

    def draw_tooltips(self, node):
        _id = "tool-" + node.get('_id')
        g = self._symbols.create_group(_id)

        hDrawTooltips = HelperDrawTooltips(self._size, self._off, self._servers)
        hDrawTooltips.execute(node)

        ltxt = hDrawTooltips.get_text()

        symbol = self._symbols.multiline(ltxt, (0,0))
        g.add(symbol)

    def grid_box(self, pos, opts={'fill-opacity': '0.4'}):
        symbol = self._symbols.asset('grid.base', 'default', pos, self._size, opts)
        self.add(symbol)

    def draw_grid_size(self, cad1, size):
        cad2 = (cad1[0], cad1[1] + size - 1)

        points = HelperDrawBasePolyline(self._size, self._matrix3d) \
            .create_polyline_by_pos(cad1, cad2)

        symbol = self._symbols.polyline(points, {'fill': '#ccc', 'fill-opacity': 0.2})
        self.add(symbol)

    def draw_root(self, item):
        root = item[3].get('root')
        if root:
            nitem = (item[0] - 1, item[1], item[2], item[3])
            pos = self._matrix3d.rotateNodeXY(nitem)()

            symbol = self._symbols.asset('grid.entry', 'default', pos, self._size)

            self.draw_connect(nitem, item)
            self.add(symbol)

    def add(self, symbol):
        self.dwg.add(symbol)

    def save(self):
        return self.dwg.tostring()

    def draw_connect(self, node1, node2, details={}):
        id = "%s-%s" % (node1[0], node2[0])
        g = self._symbols.create_group(id)

        d = HelperDrawConnector(self._size, self._off, self._matrix3d).connect(node1, node2)

        symbol = self._symbols.conn(d)
        g.add(symbol)

        cls = " conn-%s" % node1[3].get('_id')
        symbol = self._symbols.conn_holder(d, cls)
        g.add(symbol)

        symbol = self._symbols.text(details, (0,0), {'display': 'none'})
        g.add(symbol)

        self.add(g)

