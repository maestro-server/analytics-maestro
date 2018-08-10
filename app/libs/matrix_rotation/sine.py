
import math


class CalSine(object):
    cos = math.sin(math.radians(30.4))

    @staticmethod
    def cal(cat):
        hip = cat / CalSine.cos
        return math.sqrt((hip ** 2) - (cat ** 2))