import pytest
from src.board import Board, EMPTY

def test_board_init():
    b = Board()
    assert len(b.grid) == 7
    assert len(b.grid[0]) == 6
    assert all(cell == EMPTY for col in b.grid for cell in col)

def test_drop_and_undo():
    b = Board()
    row = b.drop(0, 1)
    assert row == 0
    assert b.grid[0][0] == 1
    b.undo(0)
    assert b.grid[0][0] == EMPTY

