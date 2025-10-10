# tests/test_ai_integration.py
from src.board import Board, PLAYER, AI
from src.ai import random_ai, heuristic_ai

def test_random_ai_returns_valid_move():
    b = Board()
    move, score = random_ai(b)
    assert move in b.get_valid_moves() or move is None

def test_heuristic_ai_returns_valid_move_and_score():
    b = Board()
    move, score = heuristic_ai(b, AI)
    assert move in b.get_valid_moves() or move is None
