from app.libs.grid.map import GridMap
from app.libs.patterns.iterator import IteratorMasterPattern
from app.libs.helpers.attributes import HelperDefineAttributes
from app.libs.helpers.setupWeight import HelperSetupWeight
from app.libs.helpers.orderedSucces import HelperOrderedSuccers
from app.libs.helpers.clearEmptyLines import HelperClearEmptyLines


class GridOrchestrator(object):
    def __init__(self, G, GMap=GridMap):
        self._graph = G
        self._grid = GMap()

    def get_mapping(self):
        grid = self._grid.get_grid()
        index = self._grid.get_index()
        return HelperClearEmptyLines().run(grid, index)

    def create(self, entries, SHelper=HelperSetupWeight):
        SHelper(self._graph).setup()
        self._recursive_draw(entries)

    def add_pos_grid(self, node, CIterator=IteratorMasterPattern, CHelper=HelperDefineAttributes):
        Helper = CHelper(node, self._grid, self._graph)
        CIterator(self._grid, Helper).find_rule()

        return Helper

    def _recursive_draw(self, app, i=0, OHelper=HelperOrderedSuccers):
        if i > 30:
            return

        for item in app:
            if not self._grid.in_index(item):
                node = self._graph.nodes[item]
                helper = self.add_pos_grid(node)

                succ = OHelper(helper).get_succers()
                self._recursive_draw(succ, i + 1)
