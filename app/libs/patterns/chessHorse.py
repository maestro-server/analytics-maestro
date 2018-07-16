class ChessHorsePattern(object):
    def chess_horse(self):
        succers = self._helper.only_subdirect_successors()

        if len(succers) >= 1:
            posy = self._max_empty_y(self._step)

            diff = 0
            for item in succers:
                w = self._helper.get_weight(item)
                switch_y = self.chess_horse_eligible_y(item, w)
                diff = ((w + switch_y) - self._step)

            self.chess_horse_dummie(diff, posy)
            self.balance_nodes(1)

    def chess_horse_dummie(self, diff, posy):
        for rg in range(diff):
            nstep = self._step + rg + 1

            if not self._grid.has_pos(nstep, posy):
                self._grid.create_dummy((nstep, posy))

    def chess_horse_eligible_y(self, label, w):
        diff = 0

        if self._grid.in_index(label):
            mypos = self._grid.get_index(label)
            start_search_y = mypos[1] + mypos[2]
            end_search_y = self._max_empty_y(w)

            nstep = self.chess_horse_recursive_y(start_search_y, end_search_y, mypos[0], label)
            diff = nstep - w

            if nstep != w:
                self._grid.make_swift(label, nstep)

        return diff

    def chess_horse_recursive_y(self, y1, y2, step, label):
        mx = step + 20
        while step <= mx:
            check = self.chess_horse_find_y(y1, y2, step, label)

            if check:
                break
            else:
                step += 1

        return step

    def chess_horse_find_y(self, y1, y2, step, node):
        last_node = self.find_next_node(y1, y2, step)
        return (last_node == False or last_node == node)