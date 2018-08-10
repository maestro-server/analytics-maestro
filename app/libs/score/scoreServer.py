
from .scoreSize import ScoreSize


class ScoreServer(object):
    @staticmethod
    def make_score(cpu, memory):
        return (float(cpu) * 1.5) + float(memory)

    @staticmethod
    def val_score(score):
        return ScoreSize.scored(score)