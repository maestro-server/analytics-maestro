
from app.styles.templates import mapping_style


class ManageStyle(object):

    def __init__(self, draw, smap=mapping_style):
        self.dwg = draw
        self._used_styles = []
        self._smap = smap

    def stylish(self, template):

        if template not in self._used_styles:
            tpl = self.get_template(template)
            self.attach_style(tpl)
            self._used_styles.append(template)

    def get_template(self, name, dft='default'):
        if name in self._smap:
            return self._smap[name]

        return self._smap[dft]

    def attach_style(self, styles):
        stl = self.dwg.style(styles)
        self.dwg.defs.add(stl)