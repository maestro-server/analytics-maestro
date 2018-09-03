
from app.libs.matrix_rotation.matrixRotation import MatrixRotation


class DrawArea(object):
    def __init__(self, off, size, max_x, max_y, grid, mrotation=MatrixRotation):
        self._off = off
        self._size = size
        self._max_x = max_x
        self._max_y = max_y
        self._grid = grid

        self._mrotation = mrotation(self._max_x, size, off)

    def area_x(self):
        menus = self.shw_empty() - 1

        cal = self._mrotation.cal_offx(self._max_x, self._max_y) + self._size[0]
        return cal - (menus * self._size[0])

    def area_y(self):
        return self._mrotation.cal_offy(0, self._max_y) + self._size[1]

    def area(self):
        area_x = self.area_x()
        area_y = self.area_y()
        return (area_x, area_y)

    def shw_empty(self):
        x = self._max_x
        y = self._max_y

        counter = 0

        while counter < self._max_x:
            lst = self.list_checked(counter, x, y)
            for pos in lst:
                checked = self.check_empty(*pos)
                if not checked:
                    return counter

            counter += 1
        return counter - 1

    def list_checked(self, counter, x, y):
        '''
        counter 0 -> 1 item
        counter 1 -> 2 item
        '''
        pos = set()
        if counter == 0:
            pos.add((x, y))

        if counter >= 1:
            pos.add((x, y - counter))
            pos.add((x - counter, y))

        if counter > 1:
            ct = counter - 1  # remove
            for item in range(ct, 0, -1):
                p1 = (x, y - counter + item)
                p2 = (x - counter + item, y)
                pos.add(p1)
                pos.add(p2)

        return pos

    def check_empty(self, x, y):
        obj = x in self._grid and y in self._grid[x]
        return (not obj) and (obj != '-')
