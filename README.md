HEAD
\# Puissance 4 — Projet Majeure



But

Construire un Puissance 4 en console (Python) avec IA Minimax + Alpha‑Beta, heuristique et diagnostics.



Arborescence

\- src/: code source (board, rules, ai, game)

\- tests/: tests unitaires

\- docs/: documentation et design

\- demo\_games/: logs et parties d'exemple



Premiers pas

1\. Cloner le dépôt.

2\. Créer un environnement virtuel Python 3.8+.

3\. Installer dépendances (si nécessaire).

4\. Lancer les tests : `pytest -q`.





Options CLI prévues

--depth : profondeur IA

--mode : human|ai|auto

--diag : afficher diagnostics


__________
Jeu Puissance4 — README
Description
Un projet de Puissance4 en Python avec logique du plateau, règles de victoire optimisées, tests unitaires et une interface console ASCII. Conçu pour être simple à lire, tester et étendre.

Statut actuel
Board implémenté avec drop, undo, is_valid, get_valid_moves, serialize et utilitaires.

rules.is_winning_move optimisée pour ne vérifier que l’environnement du dernier coup.

Détection de match nul via is_draw.

Tests unitaires pour Board et Rules.

Interface console ASCII avec boucle de jeu, saisie colonne, alternance joueur/IA simple.

Tous les tests passent localement.

Arborescence principale
src/board.py — implémentation de la grille et opérations du plateau.

src/rules.py — détection victoire et match nul optimisée autour du dernier coup.

src/cli.py — rendu ASCII et boucle de jeu console.

tests/test_board.py — tests unitaires pour Board.

tests/test_rules.py — tests unitaires pour les règles.

README.md — ce fichier.

docs/ — notes et design.



# jeu-puissance4
Puissance 4 — projet majeure
