class Matrix3D(MatrixRotation):
    def rotateXY(self, cad, size=1):
        if size > 1:
            nposy = (size - 1) / 2
            cad = (cad[0], cad[1] + nposy)

        res = self.cal_off(cad)

        return PosMatrix3D(self._size, res, self._off)

    def rotateNodeXY(self, node):
        cadx, cady, size, _ = node
        return self.rotateXY((cadx, cady), size)

    def cal_off(self, pos):
        x = self.cal_offx(*pos)
        y = self.cal_offy(*pos)

        return (x, y)