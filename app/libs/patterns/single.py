class SinglePattern(object):
    def set_position(self):
        start_y = self._default_y()
        self._grid.create_position((self._step, start_y), self._helper.get_id())

    def grow_node(self):
        succers = self._helper.only_direct_not_drawed()
        succers_size = len(succers)

        succers_size += self.chess_horse_growing(succers_size)

        if (succers_size >= 2):
            start_y = self._default_y()

            for ps in range(succers_size - 1):
                nps = (self._step, start_y + ps)
                self._grid.create_dummy(nps)

            self._grid.inc_size_index(self._helper.get_id(), succers_size - 1)

    def chess_horse_growing(self, succers_size):
        subsuccers = self._helper.only_subdirect_successors()
        subdirect = len(subsuccers)

        sm = 0
        sm += 1 if (subdirect >= 1) and (succers_size == 0) else 0
        sm += 1 if subdirect >= 1 else 0
        return sm
