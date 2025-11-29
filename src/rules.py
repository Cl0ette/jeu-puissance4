# src/rules.py
from src.board import EMPTY, PLAYER, AI

def _scan_from(board, col, row, piece):
    directions = [(1,0), (0,1), (1,1), (1,-1)]  # horizontal, vertical, diagonales
    for dc, dr in directions:
        path = [(col, row)]
        # vers l'avant
        c, r = col + dc, row + dr
        while 0 <= c < board.cols and 0 <= r < board.lignes and board.grid[c][r] == piece:
            path.append((c, r))
            c += dc; r += dr
        # vers l'arrière
        c, r = col - dc, row - dr
        while 0 <= c < board.cols and 0 <= r < board.lignes and board.grid[c][r] == piece:
            path.insert(0, (c, r))
            c -= dc; r -= dr
        if len(path) >= 4:
            return True, path
    return False, []

def is_winning_move(board):
    """
    Vérifie si le dernier coup est gagnant.
    Retourne (True, chemin) si victoire, sinon (False, []).
    """
    if board.last_move is not None:
        col, row, piece = board.last_move
        win, path = _scan_from(board, col, row, piece)
        if win:
            return True, path
    return False, []

def is_draw(board):
    """
    Vérifie si le plateau est plein (match nul).
    """
    return board.is_full()
