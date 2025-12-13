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
        s = heuristic(board, pion) 
        board.annuler(m)
        if meilleur_score is None or s > meilleur_score:
            meilleur_score = s
            meilleur_coup = m

    return meilleur_coup, meilleur_score

def minimax(board, depth, maximizingPlayer, pion): # développé à partir du modèle proposé par Datacamp (plateforme d’apprentissage en ligne)
    # condition d’arrêt : victoire, match nul ou profondeur atteinte
    win, _ = est_coup_gagnant(board) 
    if win or depth == 0 or board.est_plein():# puits dans le graphe
        return heuristic(board, pion) # poids heuristique appliqué aux puits

    coups = board.sont_coup_valides() # arcs sortant du noeud courant

    if maximizingPlayer:
        maxEval = float("-inf") #poids de l'arc du graphe
        for m in coups: # cherche poids maximum parmi arcs sortants
            board.jouer_coup(m, pion) # parcourt chaque arc sortant du noeud courant
            eval = minimax(board, depth-1, False, pion) # explore récursivement 
            board.annuler(m) # revient au noeud courant (comme si remontait dans un graphe)
            maxEval = max(maxEval, eval) # sélection du poids maximum
        return maxEval
    else:
        opponent = PLAYER if pion == AI_PIECE else AI_PIECE
        minEval = float("inf")
        for m in coups:
            board.jouer_coup(m, opponent)
            eval = minimax(board, depth-1, True, pion)
            board.annuler(m)
            minEval = min(minEval, eval)
        return minEval # retourne poids minimum

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