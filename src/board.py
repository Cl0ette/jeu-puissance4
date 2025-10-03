# src/board.py
ROWS = 6
COLS = 7
EMPTY = 0
PLAYER = 1
AI = 2

class Board:
    """
    Représentation du plateau en colonnes empilées (list of columns).
    Chaque colonne est une liste de hauteur `rows`, index 0 = bas.
    """

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
        if not (0 <= col < self.cols):
            raise ValueError("Colonne invalide")
        if self.heights[col] == 0:
            raise ValueError("Rien à annuler dans cette colonne")
        self.heights[col] -= 1
        row = self.heights[col]
        self.grid[col][row] = EMPTY
        self.last_move = None

    def is_full(self):
        return all(h == self.rows for h in self.heights)

    def serialize(self):
        return tuple(tuple(col) for col in self.grid)

    def copy(self):
        b = Board(self.rows, self.cols)
        b.grid = [col.copy() for col in self.grid]
        b.heights = self.heights.copy()
        b.last_move = tuple(self.last_move) if self.last_move is not None else None
        return b

    def __str__(self):
        lines = []
        for r in range(self.rows - 1, -1, -1):
            line = []
            for c in range(self.cols):
                v = self.grid[c][r]
                if v == EMPTY:
                    line.append('.')
                elif v == PLAYER:
                    line.append('X')
                else:
                    line.append('O')
            lines.append(' '.join(line))
        return '\n'.join(lines)