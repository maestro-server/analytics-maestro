class GridMapDummies(object):
    def create_dummy(self, pos):
        if not self.has_pos(*pos):
            return self._add_grid(*pos, self._dmark)