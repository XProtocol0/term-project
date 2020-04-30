import copy

class Board:
    def __init__(self, board):
        self.board = copy.deepcopy(board)

    def __str__(self):
        return '\n'.join(row.__str__() for row in self.board)

    def __repr__(self): # we we print object of this class, rather than pointing to memory location, __reper__ function helps us to show it's value.
        return f'Board({self.board.__repr__()})' 

    def __deepcopy__(self, memo):
        return Board(self.board)

    @staticmethod # makes function not belong to self. Helps us to create object. 
    def new(): ## user defined function.
        return Board([[0, 0, 0] for _ in range(3)])

    def select(self, row, col, value):
        self.board[row][col] = value

    def check(self, row, col):
        return self.board[row][col]

    def safe(self, row, col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])
