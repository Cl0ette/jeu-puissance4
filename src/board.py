lignes = 6
colones = 7
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

    def __init__(self, lignes=lignes, colones=colones):
        self.lignes = lignes
        self.colones = colones
        self.grille = [[EMPTY for _ in range(lignes)] for _ in range(colones)]  # plateau vide
        self.hauteurs = [0] * colones  # nb de pions empilés par colonne
        self.dernier_coup = None  # dernier coup joué

    def est_valide(self, colone):  # vérifie si le coup est possible
        return 0 <= colone < self.colones and self.hauteurs[colone] < self.lignes

    def sont_coup_valides(self):  # renvoie les coups valides
        return [c for c in range(self.colones) if self.est_valide(c)]

    def jouer_coup(self, colone, pion):  # ajoute un pion dans la colonne
        if not self.est_valide(colone):
            raise ValueError("Colonne invalide ou pleine")
        ligne = self.hauteurs[colone]
        self.grille[colone][ligne] = pion
        self.hauteurs[colone] += 1
        self.dernier_coup = (colone, ligne, pion)
        return ligne

    def annuler(self, colone):  # supprime le dernier coup joué  
        if not (0 <= colone < self.colones):
            raise ValueError("Colonne invalide")
        if self.hauteurs[colone] == 0:
            raise ValueError("Rien à annuler dans cette colonne")
        self.hauteurs[colone] -= 1
        ligne = self.hauteurs[colone]
        self.grille[colone][ligne] = EMPTY
        self.dernier_coup = None

    def est_plein(self):  # plateau plein ?
        return all(h == self.lignes for h in self.hauteurs)

    def fige(self):  # figer le plateau  idée ia
        return tuple(tuple(colone) for colone in self.grille)

    def copie(self):  # copie du plateau
        b = Board(self.lignes, self.colones)
        b.grille = [colone.copie() for colone in self.grille]
        b.hauteurs = self.hauteurs.copie()
        b.dernier_coup = tuple(self.dernier_coup) if self.dernier_coup is not None else None
        return b

    def __str__(self):
        lignes = []
        for r in range(self.lignes - 1, -1, -1):
            line = []
            for c in range(self.colones):
                v = self.grille[c][r]
                if v == EMPTY:
                    line.append('.')
                elif v == PLAYER:
                    line.append(ROUGE + 'X' + RESET)     # joueur en rouge
                else:
                    line.append(BLEU + 'O' + RESET)  # IA en jaune
            lignes.append(' '.join(line))
        return '\n'.join(lignes)
