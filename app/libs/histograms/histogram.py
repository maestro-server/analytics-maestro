import collections


class Histogram(object):
    def __init__(self):
        self._hist = None

    def set_collections(self, data):
        self._hist = collections.Counter(data)
        return self

    def get_counter(self):
        return dict(self._hist)

    def max_columm(self):
        if self._hist != None:
            return self._hist.most_common(1)[0]

    def max_value(self):
        n = self.max_columm()
        if n:
            return n[1]