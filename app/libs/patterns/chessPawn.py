class ChessPawnPattern(object):
    def chess_pawn(self):
        is_root = self._helper.get_node_attr('root')
        step = self._helper.get_node_attr('weight')
        posy = self._default_y()

        if is_root and step > 0:
            self._grid.create_dummy((self._step, posy), self._options.get('force_mark'))
            self._step += 1