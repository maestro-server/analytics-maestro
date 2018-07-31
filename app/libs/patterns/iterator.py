from .base import BasePattern
from .single import SinglePattern
from .balance import BalancePattern
from .chessHorse import ChessHorsePattern
from .chessPawn import ChessPawnPattern


class IteratorMasterPattern(BasePattern, SinglePattern, BalancePattern, ChessHorsePattern, ChessPawnPattern):
    def map(self):
        return ['self_balance', 'predecessors_balance', 'chess_pawn', 'chess_horse', 'soft_balance', 'child_balance', 'set_position']

    def find_rule(self):
        for check in self.map():
            getattr(self, check)()