
# src/heuristic.py
from collections import Counter
from board import EMPTY, PLAYER, AI

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

    for r in range(rows): # fenetre horizontale
        for c in range(cols - 3): # pour ne pas depasser i prend la valeur de 0 a 4 exclu pour récupérer 4 cases et le c va jusqu'a cols-3 pour que c+ i ne depasse jamais le nb de colonnes maximum 
            window = []
            for i in range(4):
                window.append(grid[c+i][r])
            window_score= score_window(window, piece)
            score += window_score



    for c in range(cols):# fenetre verticale
        for r in range(rows - 3):
            for i in range(4):
                window.append(grid[c][r + i])
           # window = [grid[c][r + i] for i in range(4)]
            score += score_window(window, piece)

        # on prend les 4 cases les une sau dessus des autres consécutive dans la colonne c et l'on calcule le score cumulé de ses cases puis l'on refait la meme chose mais en le faisant glisser de 1 crant vers le haut

    for c in range(cols - 3): # fenetre diagonale montante de gauche a droite
        for r in range(rows - 3):
            for i in range(4): 
                window.append(grid[c + i][r + i])
           # window = [grid[c + i][r + i] for i in range(4)]
            score += score_window(window, piece)

    for c in range(cols - 3):# fenetre diaginale descendente de gauche a droite
        for r in range(3, rows): 
            for i in range(4):
                window.append(grid[c + i][r - i])
            #window = [grid[c + i][r - i] for i in range(4)]
            score += score_window(window, piece)
        # d'abord on prend une colone et on choisi un groupe de case en diagonale descendente vers la droite. Il faut donc commencer a partir de la ligne 3 pour que r+i soit toujours positif et ne sorte jamais du cadre. puis on monte mais sans decaler le groupe vers la droite, on fait glisser vers haut
    return score

