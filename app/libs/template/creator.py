class Creator(object):
    def __init__(self, assets):
        self._assets = assets

    def make(self):
        points = self.get_args('points')

        if points:
            points = self.getPoints(points)
            self.set_args('points', points)

        return self._assets

    def get_args(self, label):
        return self._assets.get(label)

    def set_args(self, label, value):
        self._assets[label] = value

    def getPoints(self, points):
        prepared = []
        splitted = points.split(' ')

        tmp = None
        for item in splitted:
            if tmp:
                cons = (tmp, item)
                prepared.append(cons)
                tmp = None
            else:
                tmp = item

        return prepared