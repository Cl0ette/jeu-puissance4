# src/cli.py
from src.board import Board, EMPTY, PLAYER, AI
from src.rules import est_coup_gagnant, est_match_nul
from src import ai as ai

# Codes ANSI
RESET = "\033[0m"
ROUGE = "\033[91m"
BLEU = "\033[94m"
JAUNE = "\033[93m"  # utilisé pour mettre en évidence le chemin gagnant

SYMBOLS = {
    EMPTY: '.',
    PLAYER: ROUGE + 'X' + RESET,
    AI: BLEU + 'O' + RESET
}

def render(board: Board, chemin_gagant=None):
    """
    Affiche le plateau. Si chemin_gagant est fourni, les cases du chemin gagnant
    sont affichées en doré.
    """
    gagnant = set(chemin_gagant) if chemin_gagant else set()
    lignes = []
    for l in range(board.lignes - 1, -1, -1):
        ligne = []
        for c in range(board.colones):
            v = board.grille[c][l]
            if (c, l) in gagnant and v in (PLAYER, AI):
                ligne.append(JAUNE + ('X' if v == PLAYER else 'O') + RESET)
            else:
                ligne.append(SYMBOLS[v])
        lignes.append(' '.join(ligne))
    header = ' '.join(str(i) for i in range(board.colones))
    return header + '\n' + '\n'.join(lignes)

def demander_colonne(board: Board):
    while True:
        try:
            raw = input(f"choisir une colone (0-{board.colones-1}) ou 'q' pour quitter: ").strip()
            if raw.lower() in ('q', 'quit', 'exit'):
                return None
            colone = int(raw)
            if not board.est_valide(colone):
                print("Colone invalide. Veuillez en choisir une autre.")
                continue
            return colone
        except ValueError:
            print("Veuillez choisir un nombre s'il vous-plait.")

def choisir_mode():
    print("Choisisez un mode:")
    print("1) Joueur vs ia aléatoire")
    print("2) Joueur vs ia heuristique")
    print("3) Joueur vs ia minimax")
    while True:
        choice = input("choisisez 1, 2 ou 3 (defaut 1): ").strip() or "1"
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Entrer 1, 2 ou 3.")

def jouer_au_jeu(lignes: int = 6, colones: int = 7):
    board = Board(lignes=lignes, colones=colones)
    mode = choisir_mode()
    current = PLAYER
    while True:
        print(render(board))

        if current == PLAYER:
            colone = demander_colonne(board)
            if colone is None:
                print("le joueur a quitter la partie.")
                break
            board.jouer_coup(colone, PLAYER)
            print(f"joueur X -> colone {colone}")

            win, chemin = est_coup_gagnant(board)
            if win:
                print(render(board, chemin_gagant=chemin))
                print("le joueur X a gagné!")
                break
            current = AI

        else:
            valid = board.sont_coup_valides()
            if not valid:
                print("il n'y a plus de coup possible.")
                break

            if mode == 1:
                move, score = ai.ia_aleatoire(board)
                print(f"l'ia a choisi -> colone {move}")
            elif mode == 2:
                move, score = ai.ia_heuristique(board, AI)
                print(f"l'ia a choisi -> colone {move} avec le score {score}")
            else:
                move, score = ai.ia_minimax(board, AI)
                print(f"l'ia a choisi -> colone {move} avec le score {score}")

            if move is None:
                print("l'ia ne peut plus bouger.")
                break

            board.jouer_coup(move, AI)

            win, chemin = est_coup_gagnant(board)
            if win:
                print(render(board, chemin_gagant=chemin))
                print("l'ia O a gagnée!")
                break

            current = PLAYER

        if est_match_nul(board):
            print(render(board))
            print("Match null!")
            break

if __name__ == "__main__":
    jouer_au_jeu()
