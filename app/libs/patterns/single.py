class SinglePattern(object):
    
    def set_position(self):
        start_y = self._default_y()
        
        attr = self._helper.get_attrs()
        size = self.grow_node(start_y+1)
        self._grid.create_position((self._step, start_y), self._helper.get_id(), size, attr)

    def grow_node(self, start_y):
        size = 1
        succers = self._helper.only_direct_not_drawed()
        succers_size = len(succers)
        
        succers_size += self.chess_horse_growing(succers_size)
        
        if (succers_size >= 2):

            for ps in range(succers_size-1):
                nps = (self._step, start_y + ps)
                self._grid.create_dummy(nps)

            size = succers_size
            
        return size

    def chess_horse_growing(self, succers_size):
        subsuccers = self._helper.only_subdirect_successors()
        subdirect = len(subsuccers)

        sm = 0
        sm += 1 if (subdirect >= 1) and (succers_size == 0) else 0
        sm += 1 if subdirect >= 1 else 0
        return sm
