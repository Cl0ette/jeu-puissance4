# src/ai.py
import random
from board import PLAYER, AI as AI_PIECE
from heuristic import heuristic

# True pour voir les messages pendant la démo, False pour silence
DETAILLE = True

def affiche(msg: str, *args):
    if DETAILLE:
        print(msg % args if args else msg)

def random_ai(board):
    # liste des colonnes encore jouables
    moves = board.get_valid_moves()
    affiche("random_ai: valid moves = %s", moves)

    if not moves:
        affiche("random_ai: no valid moves")
        return None, None

    choice = random.choice(moves)
    affiche("random_ai: chosen move = %s", choice)
    return choice, 0

def heuristic_ai(board, piece):
    # teste chaque colonne, évalue, annule, et garde le meilleur
    moves = board.get_valid_moves()
    affiche("heuristic_ai: valid moves = %s", moves)
    if not moves:
        affiche("heuristic_ai: no valid moves")
        return None, None

    best_move = None
    best_score = None

    for m in moves:
        board.drop(m, piece)          # jouer le pion
        s = heuristic(board, piece)  # évaluer la position
        # on suppose que board.undo() annule le dernier coup sans argument
        # si ton board attend undo(col) remplace par board.undo(m)
        try:
            board.undo()             # annuler la simulation
        except TypeError:
            # fallback simple : essayer avec la colonne
            board.undo(m)

        affiche("heuristic_ai: move %s -> score %s", m, s)

        if best_score is None or s > best_score:
            best_score = s
            best_move = m

    affiche("heuristic_ai: chosen move = %s with score = %s", best_move, best_score)
    return best_move, best_score
