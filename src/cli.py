# src/cli.py
from src.board import Board, EMPTY, PLAYER, AI
from src.rules import is_winning_move, is_draw

SYMBOLS = {EMPTY: '.', PLAYER: 'X', AI: 'O'}

def render(board):
    lines = []
    for r in range(board.rows - 1, -1, -1):
        row = []
        for c in range(board.cols):
            row.append(SYMBOLS[board.grid[c][r]])
        lines.append(' '.join(row))
    header = ' '.join(str(i) for i in range(board.cols))
    return header + '\n' + '\n'.join(lines)

def ask_column(board):
    while True:
        try:
            raw = input(f"Choose column (0-{board.cols-1}) or 'q' to quit: ").strip()
            if raw.lower() in ('q', 'quit', 'exit'):
                return None
            col = int(raw)
            if not board.is_valid(col):
                print("Invalid column. Choose another one.")
                continue
            return col
        except ValueError:
            print("Please enter a number.")

def play_console(rows=6, cols=7):
    board = Board(rows=rows, cols=cols)
    current = PLAYER
    print("\nStarting Puissance4 (console).")
    while True:
        print(render(board))
        if current == PLAYER:
            col = ask_column(board)
            if col is None:
                print("Bye.")
                break
            board.drop(col, PLAYER)
            if is_winning_move(board):
                print(render(board))
                print("Player X wins!")
                break
            current = AI
        else:
            # simple AI: first available move
            valid = board.get_valid_moves()
            if not valid:
                print("No moves left.")
                break
            col = valid[0]
            board.drop(col, AI)
            print(f"AI places in column {col}")
            if is_winning_move(board):
                print(render(board))
                print("AI O wins!")
                break
            current = PLAYER

        if is_draw(board):
            print(render(board))
            print("Draw!")
            break

if __name__ == "__main__":
    play_console()
