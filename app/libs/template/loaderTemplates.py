
import os
import json


class LoadTemplates(object):
    def __init__(self, path):
        self._path = path
        self._mapp = {}

        self.crawler()

    def __call__(self):
        return self._mapp

    def crawler(self):
        for (dirpath, dirnames, filenames) in os.walk(self._path):
            if filenames:
                spl = dirpath.split('/')[-1]
                self.iter_files(spl, filenames)

    def without_prefix(self, label):
        spt = label.split('.')[:-1]
        return ''.join(spt)

    def get_prefix(self, pfx):
        if pfx:
            return '%s.' % pfx

        return ''

    def iter_files(self, prefix, filenames):
        for file in filenames:
            name = '%s%s/%s' % (self._path, prefix, file)
            key = '%s%s' % (self.get_prefix(prefix), self.without_prefix(file))
            with open(name) as f:
                data = json.load(f)
                self._mapp[key] = data