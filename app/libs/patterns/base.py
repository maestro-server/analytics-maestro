class BasePattern(object):
    def __init__(self, grid, Helper):
        self._helper = Helper
        self._grid = grid
        self._step = self._helper.get_step()

        self._options = {
            'max_inter': 30
        }

    def _default_y(self):
        return self._max_empty_y(self._step)

    def _max_empty_y(self, step):
        if self._grid.not_in_grid(step):
            return 0

        return self._grid.max_y(step) + 1

    def find_next_node(self, y1, y2, step):
        found = False

        for it in range(y2, y1 - 1, -1):
            if self._grid.in_grid(step) and self._grid.is_node(step, it):
                found = self._grid.get_pos(step, it)
                break

        return found