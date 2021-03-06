
from .helperDraw import HelperDraw
from app.libs.dcServer import DcServers


class HelperDrawTooltips(HelperDraw):
    def __init__(self, size, off, dcServers=DcServers):
        self._text = []
        self._pos = None
        self._app = None
        self._off = off

        self._font_size = 12
        self._dcServers = dcServers()
        super().__init__(size)

    def execute(self, app):
        self._app = app

        servers = self._app.get('servers', [])
        dc = self._dcServers.findDC(self._app)

        props = {k: self._app.get(k, None) for k in ('name', 'provider', 'family', 'environment', 'language', 'cluster')}

        self.make_text('name', props['name'])

        self.make_text('dc', dc)
        self.make_text('env', props['environment'])
        self.make_text('family', props['family'])
        self.make_text('provider', props['provider'])
        self.make_text('Language', props['language'])
        self.make_text('Cluster', props['cluster'])
        self.make_text('servers', len(servers))


    def get_text(self):
        return self._text

    def make_text(self, cls, text, opts={}):
        if text:
            dts = {
                'class_': cls,
                'text': text
            }

            obj = {**dts, **opts}
            self._text.append(obj)