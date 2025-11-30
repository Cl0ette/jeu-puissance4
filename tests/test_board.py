# tests/test_board.py
import pytest
from src.board import Board, EMPTY, PLAYER, AI

def test_board_init():
    b = Board()
    assert b.lignes == 6 and b.colones == 7
    assert len(b.grid) == 7
    assert len(b.grid[0]) == 6
    assert all(cell == EMPTY for colone in b.grid for cell in colone)
    assert b.hauteurs == [0] * 7
    assert b.last_move is None

def test_drop_and_undo():
    b = Board()
    row = b.jouer_coup(0, PLAYER)
    assert row == 0
    assert b.grid[0][0] == PLAYER
    assert b.hauteurs[0] == 1
    b.jouer_coup(0, AI)
    assert b.hauteurs[0] == 2
    b.annuler(0)
    assert b.hauteurs[0] == 1
    assert b.grid[0][1] == EMPTY
    b.annuler(0)
    assert b.hauteurs[0] == 0
    assert b.grid[0][0] == EMPTY
    with pytest.raises(ValueError):
        b.annuler(0)

def test_is_valid_and_get_valid_moves():
    b = Board(lignes=2, colones=3)
    assert b.avoir_coup_valides() == [0, 1, 2]
    b.jouer_coup(0, PLAYER)
    b.jouer_coup(0, AI)
    assert not b.est_valide(0)
    assert 0 not in b.avoir_coup_valides()
    assert set(b.avoir_coup_valides()) == {1, 2}

def test_serialize_and_copy():
    b = Board()
    b.jouer_coup(3, PLAYER)
    s = b.fige()
    assert isinstance(s, tuple)
    c = b.copie()
    c.jouer_coup(0, AI)
    assert b.fige() != c.fige()

def test_is_full():
    b = Board(lignes=2, colones=2)
    assert not b.est_plein()
    b.jouer_coup(0, PLAYER)
    b.jouer_coup(0, PLAYER)
    b.jouer_coup(1, AI)
    b.jouer_coup(1, AI)
    assert b.est_plein()
