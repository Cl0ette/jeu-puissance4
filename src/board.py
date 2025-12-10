lignes = 6   #pour modifier le nb de lignes ou de colonnes, il faut les modifié a la main dans l appel de la fonction jouer_au_jeu derniere ligne de src.cli
colonnes = 7
EMPTY = 0
PLAYER = 1
AI = 2

# Codes ANSI pour les couleurs fait a partir d une vidéo yt et ia
RESET = "\033[0m"
ROUGE = "\033[91m"
JAUNE = "\033[93m"
BLEU = "\033[94m"


class Board:
    """
    Représentation du plateau en colonnes empilées (list of columns).
    Chaque colonne est une liste de hauteur `lignes`, index 0 = bas.
    """

    def __init__(self, lignes=lignes, colonnes=colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[EMPTY for _ in range(lignes)] for _ in range(colonnes)]  # plateau vide
        self.hauteurs = [0] * colonnes  # nb de pions empilés par colonne
        self.dernier_coup = None  # dernier coup joué

    def est_valide(self, colonne):  # vérifie si le coup est possible
        return 0 <= colonne < self.colonnes and self.hauteurs[colonne] < self.lignes

    def sont_coup_valides(self):  # renvoie les coups valides
        return [c for c in range(self.colonnes) if self.est_valide(c)]

    def jouer_coup(self, colonne, pion):  # ajoute un pion dans la colonne
        if not self.est_valide(colonne):
            raise ValueError("Colonne invalide ou pleine")
        ligne = self.hauteurs[colonne]
        self.grille[colonne][ligne] = pion
        self.hauteurs[colonne] += 1
        self.dernier_coup = (colonne, ligne, pion)
        return ligne

    def annuler(self, colonne):  # supprime le dernier coup joué  
        if not (0 <= colonne < self.colonnes):
            raise ValueError("Colonne invalide")
        if self.hauteurs[colonne] == 0:
            raise ValueError("Rien à annuler dans cette colonne")
        self.hauteurs[colonne] -= 1
        ligne = self.hauteurs[colonne]
        self.grille[colonne][ligne] = EMPTY
        self.dernier_coup = None

    def est_plein(self):  # plateau plein ?
        return all(h == self.lignes for h in self.hauteurs)

    def __str__(self):
        lignes = []
        for l in range(self.lignes - 1, -1, -1):
            line = []
            for c in range(self.colonnes):
                v = self.grille[c][l]
                if v == EMPTY:
                    line.append('.')
                elif v == PLAYER:
                    line.append(ROUGE + 'X' + RESET)     # joueur en rouge
                else:
                    line.append(BLEU + 'O' + RESET)  # IA en jaune
            lignes.append(' '.join(line))
        return '\n'.join(lignes)
