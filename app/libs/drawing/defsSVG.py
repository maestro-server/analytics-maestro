class DefsSVG(object):
    def __init__(self, draw):
        self.dwg = draw

    def app(self, pos, title, size=(20, 20), unit="px"):
        opts = {
            'size': ("%s%s" % (size[0], unit), "%s%s" % (size[1], unit)),
            'stroke_width': "1",
            'stroke': "black",
            'fill': "rgb(255,255,0)"
        }

        self.add(self.dwg.rect(insert=pos, **opts))
        self.add(self.dwg.text(title, insert=(pos[0], pos[1] + 10), fill='red'))

    def line(self, cx, cy):
        opts = {
            'stroke_width': "1",
            'stroke': "black",
            'fill': "rgb(0,0,0)"
        }

        self.add(self.dwg.line(start=cx, end=cy, **opts))

    def add(self, svg):
        self.dwg.add(svg)