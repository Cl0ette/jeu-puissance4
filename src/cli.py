from src.board import Board, EMPTY, PLAYER, AI
from src.rules import est_coup_gagnant, est_match_nul
from src import ai as ai_mod

# Codes ANSI
RESET = "\033[0m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"  # utilisé pour mettre en évidence le chemin gagnant

SYMBOLS = {
    EMPTY: '.',
    PLAYER: RED + 'X' + RESET,
    AI: BLUE + 'O' + RESET
}

def render(board: Board, winning_path=None):
    """
    Affiche le plateau. Si winning_path est fourni, les cases du chemin gagnant
    sont affichées en doré.
    """
    winning = set(winning_path) if winning_path else set()
    lignes = []
    for r in range(board.lignes - 1, -1, -1):
        row = []
        for c in range(board.cols):
            v = board.grid[c][r]
            if (c, r) in winning and v in (PLAYER, AI):
                row.append(YELLOW + ('X' if v == PLAYER else 'O') + RESET)
            else:
                row.append(SYMBOLS[v])
        lignes.append(' '.join(row))
    header = ' '.join(str(i) for i in range(board.cols))
    return header + '\n' + '\n'.join(lignes)

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

def jouer_au_jeu(lignes: int = 6, cols: int = 7):
    board = Board(lignes=lignes, cols=cols)
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

            win, path = est_coup_gagnant(board)
            if win:
                print(render(board, winning_path=path))
                print("Player X wins!")
                break
            current = AI

        else:
            valid = board.get_valid_moves()
            if not valid:
                print("No moves left.")
                break

            if mode == 1:
                move, score = ai_mod.ia_aleatoire(board)
                print(f"AI chosen (random) -> col {move}")
            else:
                move, score = ai_mod.ia_heuristique(board, AI)
                print(f"AI chosen (heuristic) -> col {move} with score {score}")

            if move is None:
                print("AI cannot move.")
                break

            board.drop(move, AI)

            win, path = est_coup_gagnant(board)
            if win:
                print(render(board, winning_path=path))
                print("AI O wins!")
                break

            current = PLAYER

        if est_match_nul(board):
            print(render(board))
            print("Draw!")
            break

if __name__ == "__main__":
    jouer_au_jeu()
