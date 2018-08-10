
import math


class CalCosine(object):
    cos = math.cos(math.radians(30.4))

    @staticmethod
    def cal(cat):
        hip = cat / CalCosine.cos
        return math.sqrt((hip ** 2) - (cat ** 2))