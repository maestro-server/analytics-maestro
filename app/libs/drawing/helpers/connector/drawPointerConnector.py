
from .pathFactor import PathFactor


class HelperPointerNodeConnector(object):
    def __init__(self, matrix3d, pathFactor=PathFactor):
        self._matrix3d = matrix3d
        self._path = pathFactor()

    def get_path(self):
        return self._path()

    # front end points
    def node_mid_front(self, pos, size):
        self._factory_matrix(pos, size, 'mid', 'node', 'front')

    def point_mid_front(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'mid', 'point', 'front')

    def node_start_front(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'start', 'node', 'front', om)

    def node_end_front(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'end', 'node', 'front', om)

    def point_start_front(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'start', 'point', 'front', om)

    def point_end_front(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'end', 'point', 'front', om)

    # back end points
    def node_start_back(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'start', 'node', 'back', om)

    def node_mid_back(self, pos, size):
        self._factory_matrix(pos, size, 'mid', 'node', 'back')

    def point_mid_back(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'mid', 'point', 'back')

    def node_end_back(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'end', 'node', 'back', om)

    def point_start_back(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'start', 'point', 'back', om)

    def point_end_back(self, pos, size, om=(0, 0)):
        self._factory_matrix(pos, size, 'end', 'point', 'back', om)

    def _factory_matrix(self, pos, size, alloc='mid', point='node', view='front', om=(0, 0)):
        method = "%s_%s_%s" % (alloc, point, view)

        PoxMatrix = self._matrix3d.rotateXY(pos, size)
        npos = getattr(PoxMatrix, method)(om)
        self._path.add_point(*npos)