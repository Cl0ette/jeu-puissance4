# src/rules.py
from src.board import EMPTY, PLAYER, AI

def _scan_from(board, colone, ligne, piece):
    directions = [(1,0), (0,1), (1,1), (1,-1)]  # horizontal, vertical, diagonales
    for dc, dr in directions:
        path = [(colone, ligne)]
        # vers l'avant
        c, r = colone + dc, ligne + dr
        while 0 <= c < board.colones and 0 <= r < board.lignes and board.grille[c][r] == piece:
            path.append((c, r))
            c += dc; r += dr
        # vers l'arrière
        c, r = colone - dc, ligne - dr
        while 0 <= c < board.colones and 0 <= r < board.lignes and board.grille[c][r] == piece:
            path.insert(0, (c, r))
            c -= dc; r -= dr
        if len(path) >= 4:
            return True, path
    return False, []

def est_coup_gagnant(board):
    """
    Vérifie si le dernier coup est gagnant.
    Retourne (True, chemin) si victoire, sinon (False, []).
    """
    if board.last_move is not None:
        colone, ligne, piece = board.last_move
        win, path = _scan_from(board, colone, ligne, piece)
        if win:
            return True, path
    return False, []

def est_match_nul(board):
    """
    Vérifie si le plateau est plein (match nul).
    """
    return board.est_plein()
