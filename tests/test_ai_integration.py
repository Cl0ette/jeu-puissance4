# tests/test_ai_integration.py
from src.board import Board, PLAYER, AI
from src.ai import ia_aleatoire, ia_heuristique

def test_random_ai_returns_valid_move():
    b = Board()
    move, score = ia_aleatoire(b)
    assert move in b.sont_coup_valides() or move is None

def test_heuristic_ai_returns_valid_move_and_score():
    b = Board()
    move, score = ia_heuristique(b, AI)
    assert move in b.sont_coup_valides() or move is None
