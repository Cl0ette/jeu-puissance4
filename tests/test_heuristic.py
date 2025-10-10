# tests/test_heuristic.py
from src.board import Board, PLAYER, AI
from src.heuristic import heuristic

def test_empty_board_scores_zero():
    b = Board()
    assert heuristic(b, PLAYER) == 0

def test_center_preference():
    b = Board()
    mid = b.cols // 2
    b.drop(mid, PLAYER)
    assert heuristic(b, PLAYER) > 0
    assert heuristic(b, AI) <= 0

def test_three_in_row_advantage():
    b = Board()
    b.drop(0, PLAYER)
    b.drop(1, PLAYER)
    b.drop(2, PLAYER)
    s = heuristic(b, PLAYER)
    assert s >= 10

def test_block_opponent_three_is_negative():
    b = Board()
    b.drop(0, AI)
    b.drop(1, AI)
    b.drop(2, AI)
    s = heuristic(b, PLAYER)
    assert s < 0 or heuristic(b, AI) > heuristic(b, PLAYER)

def test_win_recognized_in_heuristic():
    b = Board()
    for c in range(4):
        b.drop(c, PLAYER)
    assert heuristic(b, PLAYER) >= 1000
