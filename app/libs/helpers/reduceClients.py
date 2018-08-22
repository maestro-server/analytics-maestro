class ReduceSystem(object):

    def __init__(self):
        self._isystem = []
        self._bags = []

    def push(self, sys):

        if (sys is not None) and isinstance(sys, list):
            for item in sys:
                _id = item.get('_id')
                if _id not in self._isystem:
                    self._isystem.append(_id)
                    self._bags.append(item)

    def get_bags(self):
        return self._bags

    def __len__(self):
        return len(self.get_bags())