# tests/test_heuristic.py
from src.board import Board, PLAYER, AI
from src.heuristic import heuristic

def test_empty_board_scores_zero():
    b = Board()
    assert heuristic(b, PLAYER) == 0

def test_center_preference():
    b = Board()
    mid = b.colones // 2
    b.jouer_coup(mid, PLAYER)
    assert heuristic(b, PLAYER) > 0
    assert heuristic(b, AI) <= 0

def test_three_in_row_advantage():
    b = Board()
    b.jouer_coup(0, PLAYER)
    b.jouer_coup(1, PLAYER)
    b.jouer_coup(2, PLAYER)
    s = heuristic(b, PLAYER)
    assert s >= 10

def test_block_opponent_three_is_negative():
    b = Board()
    b.jouer_coup(0, AI)
    b.jouer_coup(1, AI)
    b.jouer_coup(2, AI)
    s = heuristic(b, PLAYER)
    assert s < 0 or heuristic(b, AI) > heuristic(b, PLAYER)

def test_win_recognized_in_heuristic():
    b = Board()
    for c in range(4):
        b.jouer_coup(c, PLAYER)
    assert heuristic(b, PLAYER) >= 1000
