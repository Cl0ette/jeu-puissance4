# src/ia.py
import random
from src.board import PLAYER, AI as AI_PIECE
from src.rules import est_coup_gagnant
from src.heuristic import heuristic

def ia_aleatoire(board):
    """
    Choisit une colonne valide au hasard.
    Retourne (colonne choisie, score=0).
    """
    moves = board.get_valid_moves()
    if not moves:
        return None, None
    choice = random.choice(moves)
    return choice, 0

def ia_heuristique(board, piece):
    """
    IA améliorée :
    1. Si elle peut gagner immédiatement, elle joue ce coup.
    2. Sinon, si l'adversaire peut gagner au prochain coup, elle bloque.
    3. Sinon, elle utilise la fonction heuristic basée sur les fenêtres.
    Retourne (colonne choisie, score).
    """
    moves = board.get_valid_moves()
    if not moves:
        return None, None

    # 1. Coup gagnant immédiat
    for m in moves:
        board.drop(m, piece)
        win, _ = est_coup_gagnant(board)
        board.undo(m)
        if win:
            return m, 1000  # gros score pour victoire immédiate

    # 2. Bloquer l’adversaire
    opponent = PLAYER if piece == AI_PIECE else AI_PIECE
    for m in moves:
        board.drop(m, opponent)
        win, _ = est_coup_gagnant(board)
        board.undo(m)
        if win:
            return m, 900  # gros score pour blocage

    # 3. Sinon, heuristique avec fenêtres
    meilleur_score = None
    best_move = None
    for m in moves:
        board.drop(m, piece)
        s = heuristic(board, piece)  # <-- ta fonction avec les fenêtres
        board.undo(m)
        if meilleur_score is None or s > meilleur_score:
            meilleur_score = s
            best_move = m

    return best_move, meilleur_score

