from operator import itemgetter
from .helperDraw import HelperDraw
from ..microSingle import MicroCalSingle
from app.libs.dcApp import DcApps
from app.libs.score.scoreServer import ScoreServer
from app.libs.matrix_rotation.calGrid.factoryCalGrid import FactoryCalGrid

class HelperDrawApplication(HelperDraw):
    def __init__(self, size, microCal=MicroCalSingle):

        self._microsingle = microCal()

        self._apps = []
        self._calGrid = None
        self._pos = None
        self._nsize = None
        self._gsize = None

        super().__init__(size)

        self._pointed = ['application', 'cache']

    def execute(self, pos, node):
        self._pos = pos
        family = node.get('family', 'application').lower()

        if family in self._pointed:
            self.reprv_qtd(node, family)
        else:
            self.reprv_family(node, family)

    def reprv_family(self, node, family):
        self.template_apps(family, node)

    def template_apps(self, family, node):
        catsize = node.get('size', 'medium')

        family = self.slug(family)
        asset = '%s.%s' % (family, catsize)

        template = DcApps.byApps(node)

        self._calGrid = FactoryCalGrid.zero(self._size)
        self.cal_ajust()
        self.draw_applications(0, asset, template)


    def reprv_qtd(self, node, family):
        servers = node.get('servers')

        if servers:
            self.template_with_servers(servers, family)

        if not servers:
            self.template_without_servers(family, node)

    def template_with_servers(self, servers, family):
        qtd = len(servers)

        self._calGrid = FactoryCalGrid.caller(qtd, self._size)
        mx = self._calGrid.get_size()

        self.cal_ajust()

        ordered_servers = self.sorted_servers(servers, family)
        for serv in enumerate(ordered_servers):
            if mx > serv[0]:
                self.single_server(*serv)

    def template_without_servers(self, family, node):
        size = node.get('size')
        qtd = node.get('qtd', 1)

        if size == None:
            score = ScoreServer.make_score(qtd, qtd)
            size = ScoreServer.val_score(score)

        family = self.slug(family)
        asset = '%s.%s' % (family, size)
        template = DcApps.byServer(node)

        self._calGrid = FactoryCalGrid.caller(qtd, self._size)
        self.cal_ajust()

        for counter in range(qtd):
            self.draw_applications(counter, asset, template)

    def sorted_servers(self, servers, family):

        prepared = []

        for server in servers:

            if isinstance(server, dict):
                cpu = server.get('cpu', 1)
                memory = server.get('memory', 1)
                score = ScoreServer.make_score(cpu, memory)

                family = self.slug(family)
                server['asset'] = '%s.%s' % (family, ScoreServer.val_score(score))
                server['score'] = score

                prepared.append(server)

        prepared = sorted(prepared, key=itemgetter('score'), reverse=True)
        return prepared

    def single_server(self, counter, server):
        asset = server.get('asset')

        template = DcApps.byServer(server)
        self.draw_applications(counter, asset, template)

    def draw_applications(self, counter, asset, template):
        xpos, ypos = self._calGrid.get_position(counter)

        npos = (self._pos[0] + xpos, self._pos[1] + ypos)
        self.draw_symbol(npos, asset, template)

    def draw_symbol(self, pos, asset, template):
        npos = self._microsingle.get_pos(pos)
        nsize = self._microsingle.get_size(self._calGrid.get_nsize())

        app = (asset, template, npos, nsize)
        self._apps.append(app)

    def cal_ajust(self, base=0.18):
        double = self._calGrid.get_size()
        factor = (double / 100)
        inc = base - factor
        ajust = self._size[0] * inc
        self._microsingle.set_space(ajust)

    def get_apps(self):
        return self._apps

    def slug(self, str):
        return str.replace("/", '')
