from app.libs.histograms.grid import GridHistogram
from .templateSVG import DrawTemplateSVG


class DrawLayout(object):
    def __init__(self, grid, index, gridhist=GridHistogram, draw=DrawTemplateSVG):
        
        self._grid = grid
        self._index = index
        
        GridHistogram = gridhist(self._grid)
        self._nmax = GridHistogram.max_value()
        self._hist = GridHistogram.get_counter()
        
        self.drawer = draw(self._hist, self._nmax)

    def draw_nodes(self):
        data = self._grid
        for col_k, columm in data.items():
            for line_k, label in columm.items():
                if label in self._index:
                    item = self._index[label]
                    label = item[3].get('name')
                self.drawer.draw_app((col_k, line_k), col_k, label)
        
        return self
    
    def draw_connections(self, edges):
        for edge in edges:
            pos = []
            w = []
            
            for i in range(2):
                ipos = self._index[edge[i]]
                pos.append(ipos)
                w.append(ipos[0])

            self.drawer.draw_connect(*pos, *w)
            
        return self
    
    def save(self):
        self.drawer.save()