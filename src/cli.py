# src/cli.py
from src.board import Board, EMPTY, PLAYER, AI
from src.rules import est_coup_gagnant, est_match_nul
from src import ai as ai

# Codes ANSI
RESET = "\033[0m"
ROUGE = "\033[91m"
BLEU = "\033[94m"
JAUNE = "\033[93m"  # utilisé pour mettre en évidence le chemin gagnant

SYMBOLES = {
    EMPTY: '.',
    PLAYER: ROUGE + 'X' + RESET,
    AI: BLEU + 'O' + RESET
}

def afficher_plateau(board: Board, chemin_gagnant=None):
    """
    Affiche le plateau. Si chemin_gagnant est fourni, les cases du chemin gagnant
    sont affichées en doré.
    """
    gagnant = set(chemin_gagnant) if chemin_gagnant else set()
    lignes = []
    for l in range(board.lignes - 1, -1, -1):
        ligne = []
        for c in range(board.colonnes):
            v = board.grille[c][l]
            if (c, l) in gagnant and v in (PLAYER, AI):
                ligne.append(JAUNE + ('X' if v == PLAYER else 'O') + RESET)
            else:
                ligne.append(SYMBOLES[v])
        lignes.append(' '.join(ligne))
    en_tete = ' '.join(str(i) for i in range(board.colonnes))
    return en_tete + '\n' + '\n'.join(lignes)

def demander_colonne(board: Board):
    while True:
        try:
            saisie = input(f"choisir une colonne (0-{board.colonnes-1}) ou 'q' pour quitter: ").strip()
            if saisie.lower() in ('q', 'quit', 'exit'):
                return None
            colonne = int(saisie)
            if not board.est_valide(colonne):
                print("colonne invalide. Veuillez en choisir une autre.")
                continue
            return colonne
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

def jouer_au_jeu(lignes: int = 6, colonnes: int = 7):
    board = Board(lignes=lignes, colonnes=colonnes)
    mode = choisir_mode()
    joueur_actuel = PLAYER
    while True:
        print(afficher_plateau(board))

        if joueur_actuel == PLAYER:
            colonne = demander_colonne(board)
            if colonne is None:
                print("le joueur a quitter la partie.")
                break
            board.jouer_coup(colonne, PLAYER)
            print(f"joueur X -> colonne {colonne}")

            win, chemin = est_coup_gagnant(board)
            if win:
                print(afficher_plateau(board, chemin_gagnant=chemin))
                print("le joueur X a gagné!")
                break
            joueur_actuel = AI

        else:
            valid = board.sont_coup_valides()
            if not valid:
                print("il n'y a plus de coup possible.")
                break

            if mode == 1:
                coup, score = ai.ia_aleatoire(board)
                print(f"l'ia a choisi -> colonne {coup}")
            elif mode == 2:
                coup, score = ai.ia_heuristique(board, AI)
                print(f"l'ia a choisi -> colonne {coup} avec le score {score}")
            else:
                coup, score = ai.ia_minimax(board, AI)
                print(f"l'ia a choisi -> colonne {coup} avec le score {score}")

            if coup is None:
                print("l'ia ne peut plus bouger.")
                break

            board.jouer_coup(coup, AI)

            win, chemin = est_coup_gagnant(board)
            if win:
                print(afficher_plateau(board, chemin_gagnant=chemin))
                print("l'ia O a gagnée!")
                break

            joueur_actuel = PLAYER

        if est_match_nul(board):
            print(afficher_plateau(board))
            print("Match null!")
            break

if __name__ == "__main__":
    jouer_au_jeu()
