# src/ai.py
import random
from typing import Optional, Tuple
from src.board import PLAYER, AI as AI_PIECE
from src.heuristic import heuristic

def random_ai(board) -> Tuple[Optional[int], Optional[int]]:
    """Retourne une colonne aléatoire valide et score None/0."""
    moves = board.get_valid_moves()
    if not moves:
        return None, None
    choice = random.choice(moves)
    return choice, 0

def heuristic_ai(board, piece) -> Tuple[Optional[int], Optional[int]]:
    """Retourne la meilleure colonne selon la heuristique (évalue chaque move)."""
    best_score = None
    best_move = None
    moves = board.get_valid_moves()
    for m in moves:
        board.drop(m, piece)
        s = heuristic(board, piece)
        board.undo()
        if best_score is None or s > best_score:
            best_score = s
            best_move = m
    return best_move, best_score
