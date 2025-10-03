# src/rules.py
from src.board import EMPTY

def count_in_direction(grid, start_col, start_row, dc, dr, piece):
    c = start_col + dc
    r = start_row + dr
    count = 0
    cols = len(grid)
    rows = len(grid[0]) if cols > 0 else 0
    while 0 <= c < cols and 0 <= r < rows and grid[c][r] == piece:
        count += 1
        c += dc
        r += dr
    return count

def is_winning_move(board):
    if board.last_move is None:
        return False
    col, row, piece = board.last_move
    if piece == EMPTY:
        return False
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dc, dr in directions:
        cnt_pos = count_in_direction(board.grid, col, row, dc, dr, piece)
        cnt_neg = count_in_direction(board.grid, col, row, -dc, -dr, piece)
        if 1 + cnt_pos + cnt_neg >= 4:
            return True
    return False

def is_draw(board):
    return board.is_full() and not is_winning_move(board)
