import random
from board import Board


class AI:

    @staticmethod
    def move(game):
        c = 1
        while c == 1:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game.valid_move(row, col) == 1:
                c = game.valid_move(row, col)
                return row, col
            
        
        
    



