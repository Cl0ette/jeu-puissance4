# tests/test_rules.py
import pytest
from src.board import Board, PLAYER, AI
from src.rules import est_coup_gagnant, est_match_nul

def setup_horizontal_win():
    b = Board(lignes=6, colones=7)
    for c in range(4):
        b.jouer_coup(c, PLAYER)
    return b

def test_horizontal_win():
    b = setup_horizontal_win()
    assert est_coup_gagnant(b)

def test_vertical_win():
    b = Board(lignes=6, colones=7)
    for _ in range(4):
        b.jouer_coup(2, AI)
    assert est_coup_gagnant(b)

def test_diagonal_positive_slope_win():
    b = Board(lignes=6, colones=7)
    b.jouer_coup(0, PLAYER)
    b.jouer_coup(1, AI); b.jouer_coup(1, PLAYER)
    b.jouer_coup(2, AI); b.jouer_coup(2, AI); b.jouer_coup(2, PLAYER)
    b.jouer_coup(3, AI); b.jouer_coup(3, AI); b.jouer_coup(3, AI); b.jouer_coup(3, PLAYER)
    assert est_coup_gagnant(b)

def test_diagonal_negative_slope_win():
    b = Board(lignes=6, colones=7)
    b.jouer_coup(3, PLAYER)
    b.jouer_coup(2, AI); b.jouer_coup(2, PLAYER)
    b.jouer_coup(1, AI); b.jouer_coup(1, AI); b.jouer_coup(1, PLAYER)
    b.jouer_coup(0, AI); b.jouer_coup(0, AI); b.jouer_coup(0, AI); b.jouer_coup(0, PLAYER)
    assert est_coup_gagnant(b)

def test_no_false_positive():
    b = Board(lignes=6, colones=7)
    b.jouer_coup(0, PLAYER)
    b.jouer_coup(1, PLAYER)
    b.jouer_coup(2, AI)
    b.jouer_coup(3, PLAYER)
    assert not est_coup_gagnant(b)

def test_draw_detection():
    b = Board(lignes=2, colones=2)
    b.jouer_coup(0, PLAYER)
    b.jouer_coup(0, AI)
    b.jouer_coup(1, PLAYER)
    b.jouer_coup(1, AI)
    assert b.est_plein()
    assert est_match_nul(b)
