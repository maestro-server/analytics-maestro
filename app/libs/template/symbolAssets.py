
import os
import copy
from .symbol import Symbol
from .manageAssets import ManageAssets
from app.libs.template.loaderTemplates import LoadTemplates


class SymbolAssets(Symbol):
    def __init__(self, draw, path='%s/assets/symbol/', assets=LoadTemplates, manager=ManageAssets):
        super().__init__(draw)

        cwd = os.getcwd()
        self._map_assets = assets(path % cwd)()
        self._manager = manager(self)

    def default_family(self, family, dft='default'):
        fl = family.split('.')
        key = "%s.%s" % (fl[0], 'medium')

        if key not in self._map_assets:
            key = dft

        return key

    def find_assets(self, key):
        if key not in self._map_assets:
            key = self.default_family(key)

        return key

    def asset_marker(self, asset, opts={}):
        asset = self.find_assets(asset)

        if not asset in self._s_basket:
            configs = copy.deepcopy(self._map_assets[asset])
            create = self._manager.create(configs)

            viewbox = configs.get('viewBox')
            self.create_marker(asset, create, viewbox, opts)

    def asset(self, asset, template, pos, size, opts={}):
        asset = self.find_assets(asset)

        if not asset in self._s_basket:
            configs = copy.deepcopy(self._map_assets[asset])
            create = self._manager.create(configs)

            viewbox = configs.get('viewBox')
            self.create_symbol(asset, create, viewbox)

            self.set_proportion(asset, (viewbox[2], viewbox[3]))

        self._manager_style.stylish(template)
        opts['size'] = size

        if template:
            opts['class_'] = template

        return self.use_symbol(asset, pos, opts)