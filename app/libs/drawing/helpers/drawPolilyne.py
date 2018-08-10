
from .helperDraw import HelperDraw
from app.libs.matrix_rotation.cosine import CalCosine


class HelperDrawBasePolyline(HelperDraw):
    def create_polyline_by_pos(self, cad1, cad2):
        pos1 = self._matrix3d.rotateXY(cad1)()
        pos2 = self._matrix3d.rotateXY(cad2)()

        return self.append_points(pos1, pos2)

    def cal_points(self, pos, pos2, cos=CalCosine):
        sizex = self._size[0]
        h_sizex = sizex / 2
        sizey = self._size[1]

        cos = cos.cal(h_sizex)

        lst = [
            (pos[0], pos[1] + sizey - cos),
            (pos[0] + h_sizex, pos[1] + sizey - (cos * 2)),
            (pos2[0] + sizex, pos2[1] + sizey - cos),
            (pos2[0] + h_sizex, pos2[1] + sizey)
        ]

        return lst

    def append_points(self, pos1, pos2):
        return self.cal_points(pos1, pos2)