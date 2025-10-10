# src/ai.py
import random
from typing import Optional, Tuple
from src.board import PLAYER, AI as AI_PIECE
from src.heuristic import heuristic

def random_ai(board) -> Tuple[Optional[int], Optional[int]]:
    moves = board.get_valid_moves()
    if not moves:
        return None, None
    choice = random.choice(moves)
    return choice, 0

def heuristic_ai(board, piece) -> Tuple[Optional[int], Optional[int]]:
    """Évalue chaque move en simulant drop puis undo(col). Utilise undo(col) API."""
    best_score = None
    best_move = None
    moves = board.get_valid_moves()
    for m in moves:
        board.drop(m, piece)
        s = heuristic(board, piece)
        # Undo by column because Board.undo requires the column argument
        try:
            board.undo(m)
        except TypeError:
            # fallback: if undo() signature differs, try attribute last_move
            if hasattr(board, "last_move") and board.last_move is not None:
                col, _row = board.last_move
                board.undo(col)
            else:
                raise
        if best_score is None or s > best_score:
            best_score = s
            best_move = m
    return best_move, best_score
