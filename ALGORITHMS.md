# Algorithmes et IA

Ce document décrit les algorithmes utilisés dans le projet.

---

## Structures de données
- **Plateau (`Board`)** : matrice `grille[colonne][ligne]`.
- **Dernier coup** : stocké pour vérifier rapidement la victoire.
- **Fonctions principales** :
  - `sont_coup_valides()` : colonnes jouables
  - `jouer_coup()` / `annuler()` : simulation de coups
  - `est_plein()` : plateau rempli

---

## IA aléatoire
- Choisit une colonne valide au hasard.
- Complexité : O(V) (V = nombre de colonnes valides).
- Utilité : avoir une base, comparaison.

---

## IA heuristique
Chaine étape décisionnelle
1. **Coup gagnant immédiat** : si possible, jouer ce coup.
2. **Blocage** : empêcher l’adversaire de gagner au prochain coup.
3. **Heuristique** : évaluation du plateau via la fonction `heuristic`.

Heuristique :
- Analyse des fenêtres de 4 cases.
- Pondération selon :
  - Nombre de pions du joueur
  - Cases vides
  - Contrôle du centre (colonnes centrales favorisées)

---

## Minimax
- Exploration récursive de l’arbre des coups.
- **Maximizing player** : cherche score maximum.
- **Minimizing player** : cherche score minimum.
- Condition d’arrêt : victoire, match nul, profondeur atteinte.
- Évaluation : `heuristic(board, pion)`.

---

## Choix des paramètres
- Profondeur typique : 6–8 pour temps réel.
- Scores spéciaux :
  - Victoire immédiate : ~1000
  - Blocage adverse : ~900
  - Heuristique : somme des fenêtres + bonus centre
