# tests/test_rules.py
import pytest
from src.board import Board, PLAYER, AI
from src.rules import est_coup_gagnant, est_match_nul

def setup_horizontal_win():
    b = Board(lignes=6, cols=7)
    for c in range(4):
        b.drop(c, PLAYER)
    return b

def test_horizontal_win():
    b = setup_horizontal_win()
    assert est_coup_gagnant(b)

def test_vertical_win():
    b = Board(lignes=6, cols=7)
    for _ in range(4):
        b.drop(2, AI)
    assert est_coup_gagnant(b)

def test_diagonal_positive_slope_win():
    b = Board(lignes=6, cols=7)
    b.drop(0, PLAYER)
    b.drop(1, AI); b.drop(1, PLAYER)
    b.drop(2, AI); b.drop(2, AI); b.drop(2, PLAYER)
    b.drop(3, AI); b.drop(3, AI); b.drop(3, AI); b.drop(3, PLAYER)
    assert est_coup_gagnant(b)

def test_diagonal_negative_slope_win():
    b = Board(lignes=6, cols=7)
    b.drop(3, PLAYER)
    b.drop(2, AI); b.drop(2, PLAYER)
    b.drop(1, AI); b.drop(1, AI); b.drop(1, PLAYER)
    b.drop(0, AI); b.drop(0, AI); b.drop(0, AI); b.drop(0, PLAYER)
    assert est_coup_gagnant(b)

def test_no_false_positive():
    b = Board(lignes=6, cols=7)
    b.drop(0, PLAYER)
    b.drop(1, PLAYER)
    b.drop(2, AI)
    b.drop(3, PLAYER)
    assert not est_coup_gagnant(b)

def test_draw_detection():
    b = Board(lignes=2, cols=2)
    b.drop(0, PLAYER)
    b.drop(0, AI)
    b.drop(1, PLAYER)
    b.drop(1, AI)
    assert b.is_full()
    assert est_match_nul(b)
