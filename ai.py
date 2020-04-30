import random
from board import Board


class AI:

    @staticmethod
    def move(game):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if game.valid_move(row, col):
            return row, col
             
        else:
            AI.move(game)



