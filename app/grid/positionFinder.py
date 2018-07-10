class PositionFinder(object):
    def __init__(self, grid):
        self._options = {
            'max_inter': 30
        }
        self.grid = grid

    def giver_x(self, step):
        return step

    def give_pos(self, step):
        x = self.giver_x(step)
        y = self.given_y(step) if x in self.grid else 0

        return (x, y)

    def given_y(self, step, posy=0):
        found = 0

        while posy < self._options.get('max_inter'):
            if (posy not in self.grid[step]):
                found = posy
                break

            posy += 1

        return found
