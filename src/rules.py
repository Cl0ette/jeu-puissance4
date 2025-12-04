# src/rules.py
from src.board import EMPTY, PLAYER, AI

def _scan_from(board, colone, ligne, pion):
    directions = [(1,0), (0,1), (1,1), (1,-1)]  # horizontal, vertical, diagonales
    for dc, dr in directions:
        chemin = [(colone, ligne)]
        # vers l'avant
        c, r = colone + dc, ligne + dr
        while 0 <= c < board.colones and 0 <= r < board.lignes and board.grille[c][r] == pion:
            chemin.append((c, r))
            c += dc; r += dr
        # vers l'arrière
        c, r = colone - dc, ligne - dr
        while 0 <= c < board.colones and 0 <= r < board.lignes and board.grille[c][r] == pion:
            chemin.insert(0, (c, r))
            c -= dc; r -= dr
        if len(chemin) >= 4:
            return True, chemin
    return False, []

def est_coup_gagnant(board):
    """
    Vérifie si le dernier coup est gagnant.
    Retourne (True, chemin) si victoire, sinon (False, []).
    """
    if board.dernier_coup is not None:
        colone, ligne, pion = board.dernier_coup
        win, chemin = _scan_from(board, colone, ligne, pion)
        if win:
            return True, chemin
    return False, []

def est_match_nul(board):
    """
    Vérifie si le plateau est plein (match nul).
    """
    return board.est_plein()
