class HelperClearEmptyLines(object):

    def __init__(self):
        self._dmark = '-'
        self._tombstone = []
        self._swfgrid = {}
        self._swfindex = {}

    def run(self, grid, index):
        self._swfindex = index
        self.cleanning(grid)
        return self._swfgrid, self._swfindex

    def cleanning(self, grid):
        for row in grid:
            empty = True

            for line in grid[row]:
                m = grid[row][line][0]
                if (self._dmark != m):
                    empty = False
                    self.addSwf(row, grid[row])
                    break;

            if (empty):
                self._tombstone.append(row)

    def addSwf(self, row, line):
        qtd = len(self._tombstone)
        diff = row - qtd
        self._swfgrid[diff] = line

        if qtd > 0:
            self.swfIndex(qtd, line)

    def swfIndex(self, qtd, items):

        for item in items:
            uid = items[item]
            if (self._dmark != uid[0]):
                node = self._swfindex[uid]
                swft = node[0] - qtd

                self._swfindex[uid] = (swft, node[1], node[2], node[3])