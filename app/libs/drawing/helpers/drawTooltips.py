
from .helperDraw import HelperDraw
from app.libs.dcServer import DcServers


class HelperDrawTooltips(HelperDraw):
    def __init__(self, size, off):
        self._text = []
        self._pos = None
        self._app = None
        self._off = off

        self._font_size = 12
        super().__init__(size)

    def execute(self, pos, app):
        x = self._size[0] + 5
        y = (self._size[1]) / 3

        self._pos = (x, y)
        self._app = app

        dc = DcServers.byServer(self._app)
        servers = self._app.get('servers', [0])

        props = {k: self._app.get(k, None) for k in ('name', 'provider', 'family', 'environment')}

        self.make_title(props['name'][:20])

        self.make_property('DC', dc)
        self.make_property('Env', props['environment'])
        self.make_property('Family', props['family'])
        self.make_property('Provider', props['provider'])
        self.make_property('Servers', len(servers))

    def get_background(self):
        sbox = (170, 140)

        opts = {
            'class_': "tb-back",
            "rx": "3",
            "ry": "3"
        }

        bg = (self._pos, sbox, opts)
        return bg

    def get_button(self):
        sbox = (20, 140)
        npos = (self._pos[0] + 150, self._pos[1])

        opts = {
            'fill': "#000",
            "fill-opacity": "0.8",
            "rx": "3",
            "ry": "3"
        }

        btn = (npos, sbox, opts)
        return btn

    def get_text(self):
        return (self._text, self._pos)

    def make_property(self, key, value, space=(12, 3)):
        if key and value:
            dx = self._pos[0] + space[0]
            dy = self._font_size + space[1]

            label = '> %s: ' % key

            objl = self.make_text(
                label,
                {'dy': [dy], 'x': [dx], 'font_weight': 'bold'}
            )

            text = str(value).capitalize()
            objv = self.make_text(text)

            self._text.append(objl)
            self._text.append(objv)

    def make_title(self, title, space=(12, 14)):
        dx = self._pos[0] + space[0]
        dy = self._font_size + space[1]
        tfont = self._font_size + 2

        objt = self.make_text(
            title.capitalize(),
            {'font_size': tfont, 'dy': [dy], 'x': [dx], 'fill': '#fff', 'font_weight': 'bolder'}
        )

        objl = self.make_text(
            '--',
            {'dy': [self._font_size], 'x': [dx]}
        )

        self._text.append(objt)
        self._text.append(objl)

    def make_text(self, text, opts={}):
        font_size = opts.get('font_size', self._font_size)

        dts = {
            'class_': 'tfont',
            'text': text,
            'font_size': font_size
        }

        return {**dts, **opts}