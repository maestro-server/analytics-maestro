
from app.libs.matrix_rotation.cosine import CalCosine


class MicroCalSingle(object):
    def __init__(self, space=0):
        self.set_space(space)

    def set_space(self, space):
        self._space = space

    def get_pos(self, pos):
        cata = self._space
        cos = CalCosine.cal(cata)

        posx = pos[0] + (self._space / 2)
        posy = pos[1] - (cos / 2)

        return (posx, posy)

    def get_size(self, size):
        return (size[0] - self._space, size[1])