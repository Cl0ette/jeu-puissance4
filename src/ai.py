# IA pour jouer au Puissance 4, avec deux stratégies : aléatoire et heuristique améliorée
import random
from src.board import PLAYER, AI as AI_PIECE
from src.heuristic import heuristic
from src.rules import is_winning_move

def random_ai(board):
    """
    Choisit une colonne valide au hasard.
    Retourne (colonne choisie, score=0).
    """
    moves = board.get_valid_moves()
    if not moves:
        return None, None
    choice = random.choice(moves)
    return choice, 0

def heuristic_ai(board, piece):
    """
    IA améliorée :
    1. Si elle peut gagner immédiatement, elle joue ce coup.
    2. Sinon, si l'adversaire peut gagner au prochain coup, elle bloque.
    3. Sinon, elle choisit le coup avec le meilleur score heuristique.
    Retourne (colonne choisie, score).
    """
    moves = board.get_valid_moves()
    if not moves:
        return None, None

    # 1. Coup gagnant immédiat
    for m in moves:
        board.drop(m, piece)
        win, _ = is_winning_move(board)
        board.undo(m)
        if win:
            return m, 1000  # gros score pour victoire immédiate

    # 2. Bloquer l’adversaire
    opponent = PLAYER if piece == AI_PIECE else AI_PIECE
    for m in moves:
        board.drop(m, opponent)
        win, _ = is_winning_move(board)
        board.undo(m)
        if win:
            return m, 900  # gros score pour blocage

    # 3. Sinon, heuristique normale
    best_score = None
    best_move = None
    for m in moves:
        board.drop(m, piece)
        s = heuristic(board, piece)
        board.undo(m)
        if best_score is None or s > best_score:
            best_score = s
            best_move = m

    return best_move, best_score
