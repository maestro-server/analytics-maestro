from operator import itemgetter


class HelperOrderedSuccers(object):
    def __init__(self, helper):
        self._temp = []
        self._helper = helper

    def get_succers(self):
        subdirect = self._helper.only_subdirect_not_drawed()
        direct = self.make_sorted()
        return subdirect + direct

    def make_sorted(self):
        succers = self._helper.only_direct_not_drawed()

        for succer in succers:
            rating = self.find_rating(succer)
            self._temp.append((rating, succer))

        ordered = sorted(self._temp, key=itemgetter(0))
        return [i[1] for i in ordered]

    def find_rating(self, succer):
        preds = self._helper.grab_predecessors(succer)

        rating = 0
        if len(preds) >= 2:
            for pred in preds:
                score = self.score(pred, self._helper.get_id())
                rating += score

        return rating

    def score(self, pred, ignore):
        sc = 0
        if (pred != ignore):

            if (self._helper._grid.in_index(pred)):
                sc = -1
            else:
                sc = 1

        return sc
