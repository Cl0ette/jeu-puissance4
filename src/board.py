ROWS = 6
COLS = 7
EMPTY = 0
PLAYER = 1
AI = 2

class Board:
    def __init__(self, rows=ROWS, cols=COLS):
        self.rows = rows
        self.cols = cols
        self.grid = [[EMPTY for _ in range(rows)] for _ in range(cols)]
        self.heights = [0] * cols
        self.last_move = None  # (col, row, piece)

    def is_valid(self, col):
        return 0 <= col < self.cols and self.heights[col] < self.rows

    def get_valid_moves(self):
        return [c for c in range(self.cols) if self.is_valid(c)]

    def drop(self, col, piece):
        if not self.is_valid(col):
            raise ValueError("Colonne invalide ou pleine")
        row = self.heights[col]
        self.grid[col][row] = piece
        self.heights[col] += 1
        self.last_move = (col, row, piece)
        return row

    def undo(self, col):
        if not (0 <= col < self.cols) or self.heights[col] == 0:
            raise ValueError("Rien à annuler dans cette colonne")
        self.heights[col] -= 1
        row = self.heights[col]
        self.grid[col][row] = EMPTY
        self.last_move = None

    def is_full(self):
        return all(h == self.rows for h in self.heights)

    def serialize(self):
        return tuple(tuple(col) for col in self.grid)

