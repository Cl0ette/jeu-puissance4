# src/ai.py
import random
import logging
from typing import Optional, Tuple
from src.board import PLAYER, AI as AI_PIECE
from src.heuristic import heuristic

logger = logging.getLogger(__name__)

def random_ai(board) -> Tuple[Optional[int], Optional[int]]:
    """Retourne une colonne aléatoire valide et score None/0. Log des moves valides."""
    moves = board.get_valid_moves()
    logger.debug("random_ai: valid moves = %s", moves)
    if not moves:
        logger.debug("random_ai: no valid moves")
        return None, None
    choice = random.choice(moves)
    logger.info("random_ai: chosen move = %s", choice)
    return choice, 0

def heuristic_ai(board, piece) -> Tuple[Optional[int], Optional[int]]:
    """
    Évalue chaque move en simulant drop puis undo(col).
    Retourne (best_move, best_score) et logge chaque évaluation.
    """
    moves = board.get_valid_moves()
    logger.debug("heuristic_ai: valid moves = %s", moves)
    if not moves:
        logger.debug("heuristic_ai: no valid moves")
        return None, None

    best_score = None
    best_move = None
    # Évaluer chaque coup
    for m in moves:
        board.drop(m, piece)
        s = heuristic(board, piece)
        # undo en appelant undo(col) si l'API l'exige
        try:
            board.undo(m)
        except TypeError:
            # fallback si signature différente
            if hasattr(board, "last_move") and board.last_move is not None:
                col, _row = board.last_move
                board.undo(col)
            else:
                raise
        logger.debug("heuristic_ai: move %s -> score %s", m, s)
        if best_score is None or s > best_score:
            best_score = s
            best_move = m

    logger.info("heuristic_ai: chosen move = %s with score = %s", best_move, best_score)
    return best_move, best_score

