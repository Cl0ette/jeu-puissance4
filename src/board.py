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
        self.grid = [[EMPTY for i in range(rows)] for k in range(cols)] # creer le plateau vide
        self.heights = [0] * cols # permet de savoir le nb de pions empilés
        self.last_move = None  # connaitre le dernier coup joué

    def is_valid(self, col):
    
    # Vérifier que la colonne ou l on veut jouer est compris entre 0 et le nombre total de colonnes - 1
        if col < 0:
            return False
        if col >= self.cols:
            return False
        if self.heights[col] >= self.rows:
            return False
        return True
    

    def get_valid_moves(self):# renvooi la liste des coups valides
        moves = []
        for c in range(self.cols):
            if self.is_valid(c):
                moves.append(c)
        return moves


    def drop(self, col, piece):# ajoute un pion dans la colonne
        if not self.is_valid(col): #verifie que la colonne est accessible
            raise ValueError("Colonne invalide ou pleine")
        row = self.heights[col]
        self.grid[col][row] = piece
        self.heights[col] += 1
        self.last_move = (col, row, piece)
        return row

    def undo(self, col):# supprime le dernier coup joué (servira pour simulé les jets avec ia)
        if not (0 <= col < self.cols):
            raise ValueError("Colonne invalide")
        if self.heights[col] == 0:
            raise ValueError("Rien à annuler dans cette colonne")
        self.heights[col] -= 1
        row = self.heights[col]
        self.grid[col][row] = EMPTY
        self.last_move = None

    def is_full(self):
        for h in self.heights:
            if h != self.rows:
                return False
        return True


    def serialize(self): # permet de figer le plateau pour que l'on ne puisse plus y toucher 
        result = []
        for col in self.grid:
            result.append(tuple(col))
        return tuple(result)


    def copy(self): #fait une copie du plateau
        b = Board(self.rows, self.cols)
        b.grid = [col.copy() for col in self.grid]
        b.heights = self.heights.copy()
        b.last_move = tuple(self.last_move) if self.last_move is not None else None
        return b

    def __str__(self): # permet de placer les signes sur le plateau de jeu 
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