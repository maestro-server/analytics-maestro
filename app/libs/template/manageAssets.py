
from .creator import Creator


class ManageAssets(object):
    def __init__(self, symbol, creator=Creator):
        self._symbol_assets = symbol
        self._creator = creator

    def polygon(self, opt={}):
        return self._symbol_assets.dwg.polygon(**opt)

    def path(self, opts):
        return self._symbol_assets.dwg.path(**opts)

    def create(self, configs):
        objs = []
        items = configs.get('els')

        for item in items:
            args = item.get('args')
            shape = item.get('shape')
            opts = self._creator(args).make()

            obj = getattr(self, shape)(opts)
            objs.append(obj)

        return objs