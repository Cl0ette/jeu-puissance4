# Règles du jeu — Puissance 4

## Objectif
Aligner **4 pions consécutifs** de sa couleur et de son symbole dans n'importe quel direction(horizontalement, verticalement ou en diagonale) pour gagner.

---

## Plateau
- Grille de 7 colonnes × 6 lignes dans le jeu classique.
- Les pions tombent dans la case libre la plus basse de la colonne choisie.

---

## Déroulement
1. Le joueur ou l’IA choisit une colonne.
2. Le pion est inséré dans la case disponible la plus basse.
3. Après chaque coup :
   - Vérification de victoire (`est_coup_gagnant`)
   - Vérification de match nul (`est_match_nul`)
4. c'est au tour de l'autre joueur.

---

## Conditions de fin
- **Victoire** : 4 pions alignés.
- **Match nul** : plateau plein sans alignement.

---

## Variantes
- Choix de l’IA (`random`, `heuristic`, `minimax`).
- Profondeur de recherche ajustable pour minimax.
   - Dans src.cli ligne 97 `ai.ia_minimax(board, AI)` il faut ajouter en 3eme parametre la profondeur souhaiter p `ai.ia_minimax(board, AI, p)`.
- Choix du nombre de lignes et de colonnes possible.
   - Toujours dans src.cli, dernière ligne `jouer_au_jeu()` il faut rentre en parametre le nb de ligne l puis de colone c `jouer_au_jeu(l, c)`.