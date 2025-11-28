from src.board import Board, EMPTY, PLAYER, AI
from src.rules import is_winning_move, is_draw
from src import ai as ai_mod

SYMBOLS = {EMPTY: '.', PLAYER: 'X', AI: 'O'}

def render(board: Board) -> str:
    lines = []
    for r in range(board.rows - 1, -1, -1):
        row = [SYMBOLS[board.grid[c][r]] for c in range(board.cols)]
        lines.append(' '.join(row))
    header = ' '.join(str(i) for i in range(board.cols))
    return header + '\n' + '\n'.join(lines)

def ask_column(board: Board):
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

def choose_mode() -> int:
    print("Select mode:")
    print("1) Human vs Random AI")
    print("2) Human vs Heuristic AI")
    while True:
        choice = input("Choose 1 or 2 (default 1): ").strip() or "1"
        if choice in ("1", "2"):
            return int(choice)
        print("Enter 1 or 2.")

def play_console(rows: int = 6, cols: int = 7):
    board = Board(rows=rows, cols=cols)
    mode = choose_mode()
    current = PLAYER

    print(f"\nStarting Puissance4 (console). Mode: {'Random AI' if mode == 1 else 'Heuristic AI'}")

    while True:
        print(render(board))

        if current == PLAYER:
            col = ask_column(board)
            if col is None:
                print("Player exited the game.")
                break
            board.drop(col, PLAYER)
            print(f"Player X -> column {col}")

            if is_winning_move(board):
                print(render(board))
                print("Player X wins!")
                break
            current = AI

        else:
            valid = board.get_valid_moves()
            if not valid:
                print("No moves left.")
                break

            if mode == 1:
                move, score = ai_mod.random_ai(board)
                print(f"AI chosen (random) -> col {move}")
            else:
                move, score = ai_mod.heuristic_ai(board, AI)
                print(f"AI chosen (heuristic) -> col {move} with score {score}")

            if move is None:
                print("AI cannot move.")
                break

            board.drop(move, AI)

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
