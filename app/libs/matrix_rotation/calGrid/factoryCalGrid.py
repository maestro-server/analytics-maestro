
import math
from .calGridOne import CalGridOne
from .calGridFourth import CalGridFourth
from .calGridNineth import CalGridNineth
from .calGridZero import CalGridZero


class FactoryCalGrid(object):
    @staticmethod
    def zero(size):
        return CalGridZero(size)

    @staticmethod
    def caller(qtd, size):
        gsize = FactoryCalGrid.grid_size(qtd)
        grid = (CalGridOne, CalGridOne, CalGridFourth, CalGridNineth)

        if gsize < len(grid):
            call = grid[gsize]
        else:
            call = grid[-1]

        return call(size)

    @staticmethod
    def grid_size(qtd):
        return math.ceil(math.sqrt(qtd))