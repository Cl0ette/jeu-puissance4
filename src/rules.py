# src/rules.py
from src.board import EMPTY, PLAYER, AI

def scan(board, colonne, ligne, pion):
    """
    permet de retracer les chemins (utile juste pour coup gagnant)
    """
    directions = [(1,0), (0,1), (1,1), (1,-1)]  # horizontal, vertical, diagonales
    for dc, dl in directions:
        chemin = [(colonne, ligne)]
        # vers l'"avant"
        c, l = colonne + dc, ligne + dl
        while 0 <= c < board.colonnes and 0 <= l < board.lignes and board.grille[c][l] == pion:
            chemin.append((c, l))
            c += dc; l += dl
        # vers l'"arrière"
        c, l = colonne - dc, ligne - dl
        while 0 <= c < board.colonnes and 0 <= l < board.lignes and board.grille[c][l] == pion:
            chemin.insert(0, (c, l))
            c -= dc; l -= dl
        if len(chemin) >= 4:
            return True, chemin
    return False, []

def est_coup_gagnant(board):
    """
    Vérifie si le dernier coup est gagnant.
    Retourne (True, chemin) si victoire, sinon (False, []).
    """
    if board.dernier_coup is not None:
        colonne, ligne, pion = board.dernier_coup
        win, chemin = scan(board, colonne, ligne, pion)
        if win:
            return True, chemin
    return False, []

def est_match_nul(board):
    """
    Vérifie si le plateau est plein (match nul).
    """
    return board.est_plein()
