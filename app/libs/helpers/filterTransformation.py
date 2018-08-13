
from app.libs.helpers.pickId import pick_id


class FilterTransformation(object):

    def __init__(self):
        self._tab = None

    def transformation(self, data, dft={}):
        mapp = ['clients', 'systems', 'apps']

        for point in mapp:
            dfilter = data.get(point)

            if dfilter:
                self.set_type(point)
                result = getattr(self, 'trf_%s' % point)(dfilter)
                return result

        return dft

    def trf_clients(self, data):
        filter = {
            'clients._id': pick_id(data)
        }
        return filter

    def trf_systems(self, data):
        filter = {
            '_id': pick_id(data)
        }
        return filter

    def trf_apps(self, data):
        return pick_id(data)

    def is_(self, type):
        return self._tab == type

    def set_type(self, type):
        self._tab = type

