# src/heuristic.py
from collections import Counter
from src.board import EMPTY, PLAYER, AI

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
    lignes = board.lignes
    colones = board.colones
    grille = board.grille

    score = 0

    colone_centre = colones // 2
    
    def somme(): #juste pour augmenter le poids au centre
        cnt = 0
        for r in range(lignes):
            if grille[colone_centre][r] == pion:
                cnt += 1
        return cnt
    
    nbpions_centre = somme()
    score += nbpions_centre * poids_centre  # bonus pour les pions au centre

    # Fenêtres horizontales
    for r in range(lignes):
        for c in range(colones - 3):
            window = []
            for i in range(4):
                window.append(grille[c+i][r])
            score += score_window(window, pion)

    # Fenêtres verticales
    for c in range(colones):
        for r in range(lignes - 3):
            window = []
            for i in range(4):
                window.append(grille[c][r+i])
            score += score_window(window, pion)

    # Fenêtres diagonales montantes
    for c in range(colones - 3):
        for r in range(lignes - 3):
            window = []
            for i in range(4):
                window.append(grille[c+i][r+i])
            score += score_window(window, pion)

    # Fenêtres diagonales descendantes
    for c in range(colones - 3):
        for r in range(3, lignes):
            window = []
            for i in range(4):
                window.append(grille[c+i][r-i])
            score += score_window(window, pion)

    return score
