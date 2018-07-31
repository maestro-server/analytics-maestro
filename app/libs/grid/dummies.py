class GridMapDummies(object):
    def create_dummy(self, pos, tpl=''):
        if not self.has_pos(*pos):
            mark = "%s%s" % (self._dmark, tpl)
            return self._add_grid(*pos, mark)