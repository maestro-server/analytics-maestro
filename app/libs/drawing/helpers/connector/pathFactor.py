class PathFactor(object):
    def __init__(self):
        self._d = "M"

    def __call__(self):
        return self._d.strip()

    def add_point(self, x, y):
        self._d += "%s %s " % (x, y)