class PosMatrix3D(object):
    def __init__(self, size, pos, off):
        self._size = size
        self._off = off
        self._pos = pos

    def __call__(self):
        return self._pos

    def __getitem__(self, i):
        return self._pos[i]

    # ======================================== back mid
    def start_node_back(self, off=(0, 0)):
        md = self._start_back()

        pos = [self._pos[x] + md[x] - off[x] for x in range(2)]
        return pos

    def mid_node_back(self, off=(0, 0)):
        md = self._mid_back()

        pos = [self._pos[x] + md[x] for x in range(2)]
        return pos

    def end_node_back(self, off=(0, 0)):
        md = self._end_back()

        pos = [self._pos[x] + md[x] + off[x] for x in range(2)]
        return pos

    def start_point_back(self, off=(0, 0)):
        md = self._start_back()
        om = self._mid_space_back()

        pos = [self._pos[x] + md[x] + om[x] - off[x] for x in range(2)]
        return pos

    def mid_point_back(self, off=(0, 0)):
        md = self._mid_back()
        om = self._mid_space_back()

        pos = [self._pos[x] + md[x] + om[x] for x in range(2)]
        return pos

    def end_point_back(self, off=(0, 0)):
        md = self._end_back()
        om = self._mid_space_back()

        pos = [self._pos[x] + md[x] + om[x] + off[x] for x in range(2)]
        return pos

    def _start_back(self):
        ss1 = self._size[0] / 2
        cos2 = CalCosine.cal(ss1)

        x = 0
        y = self._size[1] - cos2

        return (x, y)

    def _mid_back(self):
        ss1 = self._size[0] / 4
        cos2 = CalCosine.cal(ss1)

        x = self._size[0] / 4
        y = self._size[1] - cos2

        return (x, y)

    def _end_back(self):
        ss1 = self._size[0] / 4
        cos2 = CalCosine.cal(ss1)

        x = self._size[0] / 2
        y = self._size[1]

        return (x, y)

    def _mid_space_back(self):
        sizex = (self._size[0]) / 4
        cos = CalCosine.cal(sizex)

        return (-sizex, cos)

    # ======================================== front point
    def start_node_front(self, off=(0, 0)):
        md = self._start_front()

        pos = [self._pos[x] + md[x] - off[x] for x in range(2)]
        return pos

    def mid_node_front(self, off=(0, 0)):
        md = self._mid_front()

        pos = [self._pos[x] + md[x] for x in range(2)]
        return pos

    def end_node_front(self, off=(0, 0)):
        md = self._end_front()

        pos = [self._pos[x] + md[x] + off[x] for x in range(2)]
        return pos

    def start_point_front(self, off=(0, 0)):
        md = self._start_front()
        om = self._mid_space_front()

        pos = [self._pos[x] + md[x] + om[x] - off[x] for x in range(2)]
        return pos

    def end_point_front(self, off=(0, 0)):
        md = self._end_front()
        om = self._mid_space_front()

        pos = [self._pos[x] + md[x] + om[x] + off[x] for x in range(2)]
        return pos

    def mid_point_front(self, off=(0, 0)):
        md = self._mid_front()
        om = self._mid_space_front()

        pos = [self._pos[x] + md[x] + om[x] for x in range(2)]
        return pos

    def _start_front(self):
        ss = self._size[0] / 2
        cos1 = CalCosine.cal(ss)

        x = self._size[0] - (self._size[0] / 2)
        y = self._size[1] - (cos1 * 2)

        return (x, y)

    def _mid_front(self):
        ss = self._size[0] / 2
        cos1 = CalCosine.cal(ss)

        x = self._size[0] - (self._size[0] / 4)
        y = self._size[1] - (cos1 * 1.5)

        return (x, y)

    def _end_front(self):
        ss = self._size[0] / 2
        cos1 = CalCosine.cal(ss)

        x = self._size[0]
        y = self._size[1] - cos1

        return (x, y)

    def _mid_space_front(self):
        sizex = (self._size[0]) / 4
        cos = CalCosine.cal(sizex)

        return (sizex, -cos)