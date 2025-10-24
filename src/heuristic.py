
# src/heuristic.py
from collections import Counter
from src.board import EMPTY, PLAYER, AI

SCORE_FOUR = 1000
SCORE_THREE = 10
SCORE_TWO = 1
CENTER_WEIGHT = 3

def score_window(window, piece): # systeme de récompense en fonction du nb de piece dans une zone
    if piece == AI:
        opp = PLAYER
    else:
        opp = AI
    # opp = PLAYER if piece == AI else AI
    cnt = Counter(window)
    if cnt[piece] == 4:
        return SCORE_FOUR
    elif cnt[piece] == 3 and cnt[EMPTY] == 1:
        return SCORE_THREE
    elif cnt[piece] == 2 and cnt[EMPTY] == 2:
        return SCORE_TWO
    elif cnt[opp] == 3 and cnt[EMPTY] == 1:
        return -SCORE_THREE
    elif cnt[opp] == 4:
        return -SCORE_FOUR
    return 0

def heuristic(board, piece):
    rows = board.rows
    cols = board.cols
    grid = board.grid

    score = 0

    center_col = cols // 2
    
    def somme():
        cnt=0
        for r in range(rows):
            if grid[center_col][r] == piece:
                cnt+=1
        return cnt
    
    center_count=somme()

    #center_count = sum(1 for r in range(rows) if grid[center_col][r] == piece)
    score += center_count * CENTER_WEIGHT # on multiplie par un facteur en plus (center weight) parce que le milieu est plus important

    for r in range(rows):
        for c in range(cols - 3):
            window = []
            for i in range(4):
                quad= grid[c+i][r]
                window.append(quad)
            window_score= score(window, piece)
            score += window_score



    for c in range(cols):
        for r in range(rows - 3):
            window = [grid[c][r + i] for i in range(4)]
            score += score_window(window, piece)

    for c in range(cols - 3):
        for r in range(rows - 3):
            window = [grid[c + i][r + i] for i in range(4)]
            score += score_window(window, piece)

    for c in range(cols - 3):
        for r in range(3, rows):
            window = [grid[c + i][r - i] for i in range(4)]
            score += score_window(window, piece)

    return score

