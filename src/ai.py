# L'IA pour jouer au jeu, avec deux stratégies : aléatoire et heuristique
import random
import logging
from typing import Optional, Tuple
from src.board import PLAYER, AI as AI_PIECE
from src.heuristic import heuristic

logger = logging.getLogger(__name__)

def random_ai(board) -> Tuple[Optional[int], Optional[int]]:
    """Retourne une colonne aléatoire valide et score 0. Log des moves valides."""
    moves = board.get_valid_moves()
    logger.debug("random_ai: valid moves = %s", moves)
    if not moves:
        logger.debug("random_ai: no valid moves")
        return None, None
    choice = random.choice(moves)
    logger.info("random_ai: chosen move = %s", choice)
    return choice, 0

def heuristic_ai(board, piece) -> Tuple[Optional[int], Optional[int]]:
    """Évalue chaque move en simulant drop puis undo(col)."""
    moves = board.get_valid_moves()
    logger.debug("heuristic_ai: valid moves = %s", moves)
    if not moves:
        logger.debug("heuristic_ai: no valid moves")
        return None, None

    best_score = None
    best_move = None
    for m in moves:
        board.drop(m, piece)
        s = heuristic(board, piece)
        board.undo(m)
        logger.debug("heuristic_ai: move %s -> score %s", m, s)
        if best_score is None or s > best_score:
            best_score = s
            best_move = m

    logger.info("heuristic_ai: chosen move = %s with score = %s", best_move, best_score)
    return best_move, best_score
