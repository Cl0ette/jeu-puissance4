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
    coups = board.sont_coup_valides()
    if not coups:
        return None, None
    choice = random.choice(coups)
    return choice, 0

def ia_heuristique(board, pion):
    """
    IA qui utilise notre heuristique :
    1. Si elle peut gagner immédiatement, elle joue le coup gagnant.
    2. Si l'adversaire peut gagner elle le bloque.
    3. Et sinon elle utilise la fonction heuristic qui "note" le plateau.
    Retourne (colonne choisie, score).
    """
    coups = board.sont_coup_valides()
    if not coups:
        return None, None

    # 1. Coup gagnant immédiat
    for m in coups:
        board.jouer_coup(m, pion)
        win, _ = est_coup_gagnant(board)
        board.annuler(m)
        if win:
            return m, 1000  # gros score pour victoire immédiate

    # 2. Bloquer l’adversaire
    opponent = PLAYER if pion == AI_PIECE else AI_PIECE
    for m in coups:
        board.jouer_coup(m, opponent)
        win, _ = est_coup_gagnant(board)
        board.annuler(m)
        if win:
            return m, 900  # gros score pour blocage

    # 3. Sinon, heuristique avec fenêtres
    meilleur_score = None
    meilleur_coup = None
    for m in coups:
        board.jouer_coup(m, pion)
        s = heuristic(board, pion)  # <-- ta fonction avec les fenêtres
        board.annuler(m)
        if meilleur_score is None or s > meilleur_score:
            meilleur_score = s
            meilleur_coup = m

    return meilleur_coup, meilleur_score

def minimax(board, depth, maximizingPlayer, pion):
    # condition d’arrêt : victoire, match nul ou profondeur atteinte
    win, _ = est_coup_gagnant(board)
    if win or depth == 0 or board.est_plein():
        return heuristic(board, pion)

    coups = board.sont_coup_valides()

    if maximizingPlayer:
        maxEval = float("-inf")
        for m in coups:
            board.jouer_coup(m, pion)
            eval = minimax(board, depth-1, False, pion)
            board.annuler(m)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        opponent = PLAYER if pion == AI_PIECE else AI_PIECE
        minEval = float("inf")
        for m in coups:
            board.jouer_coup(m, opponent)
            eval = minimax(board, depth-1, True, pion)
            board.annuler(m)
            minEval = min(minEval, eval)
        return minEval

def ia_minimax(board, pion, depth=5):
    coups = board.sont_coup_valides()
    meilleur_score = float("-inf")
    meilleur_coup = None
    for m in coups:
        board.jouer_coup(m, pion)
        score = minimax(board, depth-1, False, pion)
        board.annuler(m)
        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = m
    return meilleur_coup, meilleur_score