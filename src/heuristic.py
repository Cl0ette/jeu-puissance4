# src/heuristic.py
from collections import Counter
from src.board import EMPTY, PLAYER, AI
from src.rules import est_coup_gagnant

score_quatre = 1000
score_trois = 10
score_deux = 1
poids_centre = 2

def score_window(window, pion):  # système de récompense en fonction du nb de pion dans une zone
    if pion == AI:
        adv = PLAYER
    else:
        adv = AI
    cnt = Counter(window)
    if cnt[pion] == 4:
        return score_quatre
    elif cnt[pion] == 3 and cnt[EMPTY] == 1:
        return score_trois
    elif cnt[pion] == 2 and cnt[EMPTY] == 2:
        return score_deux
    elif cnt[adv] == 3 and cnt[EMPTY] == 1:
        return -score_trois
    elif cnt[adv] == 4:
        return -score_quatre
    return 0

def heuristic(board, pion):
    """
    fonction qui permet de noter chacunes 
    """
    lignes = board.lignes
    colonnes = board.colonnes
    grille = board.grille

    score = 0

    colone_centre = colonnes // 2
    
    def somme(): #juste pour augmenter le poids au centre
        cnt = 0
        for l in range(lignes):
            if grille[colone_centre][l] == pion:
                cnt += 1
        return cnt
    
    nbpions_centre = somme()
    score += nbpions_centre * poids_centre  # bonus pour les pions au centre

    # Fenêtres horizontales
    for l in range(lignes):
        for c in range(colonnes - 3):
            window = []
            for i in range(4):
                window.append(grille[c+i][l])
            score += score_window(window, pion)

    # Fenêtres verticales
    for c in range(colonnes):
        for l in range(lignes - 3):
            window = []
            for i in range(4):
                window.append(grille[c][l+i])
            score += score_window(window, pion)

    # Fenêtres diagonales montantes
    for c in range(colonnes - 3):
        for l in range(lignes - 3):
            window = []
            for i in range(4):
                window.append(grille[c+i][l+i])
            score += score_window(window, pion)

    # Fenêtres diagonales descendantes
    for c in range(colonnes - 3):
        for l in range(3, lignes):
            window = []
            for i in range(4):
                window.append(grille[c+i][l-i])
            score += score_window(window, pion)

    return score

