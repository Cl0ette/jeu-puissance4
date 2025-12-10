# Règles du jeu — Puissance 4

## Objectif
Aligner **4 pions consécutifs** de sa couleur et de son symbole (horizontalement, verticalement ou en diagonale).

---

## Plateau
- Grille de 7 colonnes × 6 lignes.
- Les pions tombent dans la case libre la plus basse de la colonne choisie.

---

## Déroulement
1. Le joueur ou l’IA choisit une colonne.
2. Le pion est inséré dans la case disponible la plus basse.
3. Après chaque coup :
   - Vérification de victoire (`est_coup_gagnant`)
   - Vérification de match nul (`est_match_nul`)

---

## Conditions de fin
- **Victoire** : 4 pions alignés.
- **Match nul** : plateau plein sans alignement.

---

## Variantes
- Choix de l’IA (`random`, `heuristic`, `minimax`).
- Profondeur de recherche ajustable pour minimax.
- Choix du nombre de lignes et de colonnes possible

