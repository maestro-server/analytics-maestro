
import os
import errno
import re
import json
import xml.etree.ElementTree as ET


class ConvertXMLtoJsonSVG(object):

    def __init__(self):
        self._els = []
        self.allowed = ['polygon', 'path', 'polyline']

        self._crelation = {}

        self.mapp = {
            'c4692c': 'dark',
            'f58536': 'light',
            'a0501a': 'darker',
            '723710': '2darker',
            'fff': 'white',
            'ffffff': 'white',
            'd1d1d1': 'gray',
            'bababa': 'gdarker',
            '000': 'black',
            'ccc': 'lgray',
            '6d6d6d': 'gray2',
            '3a3a3a': 'dark-gray',
            '757575': 'dark-gray2',
            'efefef': 'little-white',
            'f2f2f2': 'light-gray',
            '212121': 'light-black'
        }

    def run(self, xml):
        for item in xml:
            name = item.tag.split('}')[-1]
            content = item.attrib

            if name == 'defs':
                self.class_manager(item[0].text)

            if name in self.allowed:
                el = self.create_el(name, content)
                self._els.append(el)

        return self._els

    def create_el(self, name, el):
        cls = el.pop('class')
        ncls = self.get_rel(cls)
        if ncls:
            el['class_'] = ncls

        return {
            "args": el,
            "shape": name
        }

    def get_rel(self, cls):
        if cls in self._crelation:
            color = self._crelation[cls]
            return self.get_color(color)
        else:
            print("============================================ relation color not found - %s" %cls)


    def get_color(self, color):
        if color in self.mapp:
            return self.mapp[color]
        else:
            print("============================================ color not found - %s" %color)

    def class_manager(self, defs):
        lines = defs.split('}')
        for cc in lines:
            rr = re.search(r'\.(.*){fill:#(.*);', cc.strip())
            if rr:
                a = rr.group(1)
                b = rr.group(2)
                self._crelation[a] = b


class XMLGetViewBox(object):

    def getViewBox(self, root):

        attr = root.attrib
        if 'viewBox' in attr:
            arr = attr['viewBox'].split(' ')
            return [float(i) for i in arr]

class Crawler(object):

    def __init__(self, path, dest):
        self._path = path
        self._dest = dest

        self._result = {
            'viewBox': [],
            'els': []
        }

    def iter_folders(self, folders):
        for folder in folders:
            self.create_folder(folder)

    def create_folder(self, directory):

        full = "%s/%s" % (self._dest, directory)
        try:
            os.makedirs(full)
            print("== Create %s" % full)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def iter_files(self, prefix, filenames):
        for file in filenames:
            rr = re.search(r'(.*)\.svg', file)
            if rr:
                self.create_file(prefix, file)

    def create_file(self, prefix, filenames):

        file = "%s/%s/%s" % (self._path, prefix, filenames)
        print("file path - %s" % file)

        tree = ET.parse(file)
        root = tree.getroot()

        self._result['viewBox'] = XMLGetViewBox().getViewBox(root)
        self._result['els'] = ConvertXMLtoJsonSVG().run(root)


        filename = filenames.split('.')[0] + '.json'
        print(filename)
        self.io_json(prefix, filename, self._result)




    def io_json(self, prefix, filename, data):

        dest = "%s/%s/%s" % (self._dest, prefix, filename)
        with open(dest, 'w') as outfile:
            json.dump(data, outfile)


    def run(self):

        for (dirpath, dirnames, filenames) in os.walk(self._path):

            if dirnames:
                print("== Starting to create first level folders")
                self.iter_folders(dirnames)
            if filenames:
                print("== Starting to create files")
                spl = dirpath.split('/')[-1]
                self.iter_files(spl, filenames)

if __name__ == "__main__":

    cwd = os.getcwd()
    path = "%s/svgs/" % (cwd)
    dest = "%s/../assets/symbol/" % (cwd)

    Crawler(path, dest).run()