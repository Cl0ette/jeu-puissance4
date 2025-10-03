# tests/test_board.py
import pytest
from src.board import Board, EMPTY, PLAYER, AI

def test_board_init():
    b = Board()
    assert b.rows == 6 and b.cols == 7
    assert len(b.grid) == 7
    assert len(b.grid[0]) == 6
    assert all(cell == EMPTY for col in b.grid for cell in col)
    assert b.heights == [0] * 7
    assert b.last_move is None

def test_drop_and_undo():
    b = Board()
    row = b.drop(0, PLAYER)
    assert row == 0
    assert b.grid[0][0] == PLAYER
    assert b.heights[0] == 1
    b.drop(0, AI)
    assert b.heights[0] == 2
    b.undo(0)
    assert b.heights[0] == 1
    assert b.grid[0][1] == EMPTY
    b.undo(0)
    assert b.heights[0] == 0
    assert b.grid[0][0] == EMPTY
    with pytest.raises(ValueError):
        b.undo(0)

def test_is_valid_and_get_valid_moves():
    b = Board(rows=2, cols=3)
    assert b.get_valid_moves() == [0, 1, 2]
    b.drop(0, PLAYER)
    b.drop(0, AI)
    assert not b.is_valid(0)
    assert 0 not in b.get_valid_moves()
    assert set(b.get_valid_moves()) == {1, 2}

def test_serialize_and_copy():
    b = Board()
    b.drop(3, PLAYER)
    s = b.serialize()
    assert isinstance(s, tuple)
    c = b.copy()
    c.drop(0, AI)
    assert b.serialize() != c.serialize()

def test_is_full():
    b = Board(rows=2, cols=2)
    assert not b.is_full()
    b.drop(0, PLAYER)
    b.drop(0, PLAYER)
    b.drop(1, AI)
    b.drop(1, AI)
    assert b.is_full()
