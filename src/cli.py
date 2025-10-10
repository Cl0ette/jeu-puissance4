# src/cli.py
# Interface console ASCII pour Puissance4 avec modes Human vs AI
# - Affiche la grille
# - Permet la saisie de colonne (0..cols-1) ou 'q' pour quitter
# - Propose 2 modes d'IA : random et heuristic
# - Affiche des logs de diagnostic (moves valides, scores évalués)
#
# Sauvegarde ce fichier en UTF-8.

import logging
from src.board import Board, EMPTY, PLAYER, AI
from src.rules import is_winning_move, is_draw
from src import ai as ai_mod

# Configuration logging: DEBUG pour tout voir, changer en INFO pour moins de verbosité.
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Symboles affichés dans la grille
SYMBOLS = {EMPTY: '.', PLAYER: 'X', AI: 'O'}


def render(board: Board) -> str:
    """
    Retourne une représentation ASCII de la grille.
    - Affiche d'abord les indices de colonnes (0 .. cols-1)
    - Affiche les lignes de la plus haute à la plus basse
    """
    lines = []
    for r in range(board.rows - 1, -1, -1):
        row = []
        for c in range(board.cols):
            row.append(SYMBOLS[board.grid[c][r]])
        lines.append(' '.join(row))
    header = ' '.join(str(i) for i in range(board.cols))
    return header + '\n' + '\n'.join(lines)


def ask_column(board: Board):
    """
    Invite l'utilisateur à saisir une colonne valide ou 'q' pour quitter.
    - Retourne un int (col) ou None si l'utilisateur veut quitter.
    - Valide que la colonne est un entier et qu'elle est valide selon board.is_valid.
    """
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
    """
    Propose le choix de mode au lancement:
    1) Human vs Random AI
    2) Human vs Heuristic AI
    Retourne 1 ou 2.
    """
    print("Select mode:")
    print("1) Human vs Random AI")
    print("2) Human vs Heuristic AI")
    while True:
        choice = input("Choose 1 or 2 (default 1): ").strip() or "1"
        if choice in ("1", "2"):
            return int(choice)
        print("Enter 1 or 2.")


def play_console(rows: int = 6, cols: int = 7):
    """
    Boucle principale du jeu en console:
    - Initialise le board
    - Alterne entre PLAYER (saisie) et AI (selon mode choisi)
    - Affiche la grille avant chaque coup
    - Logge les moves valides et les scores évalués par l'IA (mode heuristique)
    - Détecte victoire et match nul
    """
    board = Board(rows=rows, cols=cols)
    mode = choose_mode()
    current = PLAYER
    logger.info("\nStarting Puissance4 (console). Mode: %s", "Random AI" if mode == 1 else "Heuristic AI")

    while True:
        # Affiche la grille à chaque itération
        print(render(board))

        if current == PLAYER:
            # Tour du joueur humain
            col = ask_column(board)
            if col is None:
                logger.info("Player exited the game.")
                break
            board.drop(col, PLAYER)
            logger.info("Player X -> column %s", col)

            # Vérifier victoire humaine
            if is_winning_move(board):
                print(render(board))
                logger.info("Player X wins!")
                break
            current = AI

        else:
            # Tour de l'IA
            valid = board.get_valid_moves()
            logger.debug("AI debug: valid moves = %s", valid)
            if not valid:
                logger.info("No moves left.")
                break

            if mode == 1:
                # IA aléatoire
                move, score = ai_mod.random_ai(board)
                logger.info("AI chosen (random) -> col %s", move)
            else:
                # IA heuristique: la fonction elle-même logge chaque évaluation (DEBUG)
                move, score = ai_mod.heuristic_ai(board, AI)
                logger.info("AI chosen (heuristic) -> col %s with score %s", move, score)

            if move is None:
                logger.info("AI cannot move.")
                break

            board.drop(move, AI)

            # Vérifier victoire IA
            if is_winning_move(board):
                print(render(board))
                logger.info("AI O wins!")
                break

            current = PLAYER

        # Vérifier match nul après chaque tour complet
        if is_draw(board):
            print(render(board))
            logger.info("Draw!")
            break


if __name__ == "__main__":
    # Lance la boucle console si exécuté comme script.
    # Pour la tester depuis PowerShell:
    # .venv\Scripts\Activate
    # python -m src.cli
    play_console()
