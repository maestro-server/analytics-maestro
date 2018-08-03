class BalancePattern(object):

    def soft_balance(self, step_pace=1):
        subsuccers = self._helper.only_subdirect_successors()
        succers = self._helper.only_direct_not_drawed()
        succers_size = len(succers + subsuccers)

        start_y = self._default_y()

        nstep = self._step + step_pace
        nposy = self._max_empty_y(nstep)

        if (succers_size > 0) and (start_y > nposy):
            diff = start_y - nposy
            for i in range(diff):
                posy = nposy + i
                self._grid.create_dummy((nstep, posy))

    def self_balance(self, step_pace=0):
        subsuccers = self._helper.only_subdirect_successors()
        succers = self._helper.only_direct_not_drawed()
        succers_size = len(succers + subsuccers)

        start_y = self._default_y()

        nstep = self._step + step_pace
        nposy = self._max_empty_y(nstep)

        if (start_y < nposy):
            diff = nposy - start_y
            for i in range(diff):
                posy = start_y + i
                self._grid.create_dummy((self._step, posy))

            self.balance_nodes(diff)

    def predecessors_balance(self, step_pace=1):
        preds = self._helper.grab_drawed_predecers()
        succers_size = len(preds)

        if succers_size > 0:
            pred = self._grid.get_index(preds[0])
            nposy = pred[1]
            start_y = self._default_y()

            if (start_y < nposy):
                diff = nposy - start_y
                for i in range(diff):
                    posy = start_y + i
                    self._grid.create_dummy((self._step, posy))

    def child_balance(self):
        succers = self._helper.only_direct_not_drawed()
        succers_size = len(succers)

        if succers_size >= 2:
            self.balance_nodes(succers_size - 1)

    def balance_nodes(self, qtd):
        for nl in range(self._step):
            last = self._max_empty_y(nl)
            for np in range(qtd):
                posy = last + np
                self._grid.create_dummy((nl, posy), self._options.get('grow_mark'))

            anode = self.find_next_node(0, last + 1, nl)
            if anode:
                self._grid.inc_size_index(anode, qtd)