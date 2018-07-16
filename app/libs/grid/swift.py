class GridMapSwift(object):
    def make_swift(self, node, loc):
        pos = self.get_index(node)
        max_x = self.max_x()
        diff = loc - pos[0]

        for columm in range(max_x, pos[0] - 1, -1):
            end = pos[1] + pos[2]

            for line in range(pos[1], end):
                self.swift_update_line(columm, line, diff)

    def swift_update_line(self, columm, line, diff):
        if line in self._grid[columm]:
            ccnode = self.get_pos(columm, line)
            self.del_grid(columm, line)

            self.swift_update_node(ccnode, diff)

    def swift_update_node(self, ccnode, diff):
        if ccnode in self._index:
            npos = self.get_index(ccnode)
            self.del_item(ccnode)

            self.create_position((npos[0] + diff, npos[1]), ccnode, npos[2])