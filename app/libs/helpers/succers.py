class HelperDefineSuccersPredecessors(object):
    def successors(self):
        return (self.only_direct_successors(), self.only_subdirect_successors())

    def only_direct_successors(self):
        self.categorize_successors()
        return self._direct_succers

    def only_subdirect_successors(self):
        self.categorize_successors()
        return self._subdirect_succers

    def only_direct_not_drawed(self, cat='direct'):
        self.categorize_successors()
        return self._succers_not_drawing.get(cat)

    def only_subdirect_not_drawed(self, cat='subdirect'):
        self.categorize_successors()
        return self._succers_not_drawing.get(cat)

    def categorize_successors(self):
        succers = set(self._graph.successors(self.get_id()))

        if (len(succers) > 0) and (not self._direct_succers):
            for node in succers:
                wg = self.get_weight(node)

                diff = wg - self._step
                self.grab_direct_succers(diff, node)
                self.grab_subdirect_succers(diff, node)

    def grab_direct_succers(self, diff, node):
        if (diff <= 1) and (node not in self._direct_succers):
            self._direct_succers.append(node)
            self.grab_not_drawing(node, 'direct')

    def grab_subdirect_succers(self, diff, node):
        if (diff > 1) and (node not in self._subdirect_succers):
            self._subdirect_succers.append(node)
            self.grab_not_drawing(node, 'subdirect')

    def grab_not_drawing(self, node, var):
        if not self._grid.in_index(node):
            self._succers_not_drawing[var].append(node)

    def direct_predecessors(self):
        if not self._predecessors:
            self._predecessors = set(self._graph.predecessors(self.get_id()))

        return self._predecessors

    def grab_drawed_predecers(self):
        preds = self.direct_predecessors()
        dpreds = []

        if len(preds) > 0:
            for node in preds:
                if self._grid.in_index(node):
                    dpreds.append(node)

        return dpreds

    def grab_predecessors(self, node):
        return set(self._graph.predecessors(node))