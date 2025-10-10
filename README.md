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
_______________________________________
Puissance4 — projet Python
Description

Implementation d’un jeu Puissance4 en Python : plateau, règles, heuristique et interface console ASCII.

Statut actuel

Board : drop, undo, is_valid, get_valid_moves, serialize (tests unitaires présents).

Rules : is_winning_move optimisée autour du dernier coup, is_draw (tests présents).

CLI : src/cli.py — rendu ASCII et boucle de jeu console (saisie colonne, alternance, quit).

Heuristique : src/heuristic.py — fenêtres de 4, pondération du centre, scores pour 4/3/2 pièces.

Tests : tests pour Board, Rules et Heuristic (pytest).

Arborescence

src/board.py

src/rules.py

src/heuristic.py

src/cli.py

tests/test_board.py

tests/test_rules.py

tests/test_heuristic.py

docs/

Installation

Ouvrir le projet: cd C:\Users\cloeh\jeu-puissance4

Activer l’environnement: .venv\Scripts\Activate

Installer dépendances: python -m pip install -U pip python -m pip install pytest

Exécution des tests

Lancer tous les tests : python -m pytest -q

Lancer la boucle console

Démarrer une partie en console : python -m src.cli

Commandes :

entrer un numéro de colonne pour jouer

entrer q pour quitter

IA : choix du premier coup valide (IA basique)

Notes d’implémentation

Heuristique : analyse toutes les fenêtres de longueur 4 (horizontales, verticales, diagonales), applique des scores pour 4/3/2 en faveur ou contre, et renforce la présence au centre pour favoriser positions centrales.

Détection victoire : is_winning_move ne vérifie que l’entourage du dernier coup, complexité constante par coup.

Stockage : grille par colonnes pour simplifier drop/undo.

________________________________________
# Puissance4 — projet Python

Description
- Implementation d’un jeu Puissance4 en Python : plateau, règles, heuristique et interface console ASCII.

Statut actuel
- Board : drop, undo, is_valid, get_valid_moves, serialize (tests unitaires présents).
- Rules : is_winning_move optimisée autour du dernier coup, is_draw (tests présents).
- CLI : src/cli.py — rendu ASCII et boucle de jeu console (saisie colonne, alternance, quit).
- Heuristique : src/heuristic.py — fenêtres de 4, pondération du centre, scores pour 4/3/2 pièces.
- AI : src/ai.py — IA aléatoire et IA heuristique (évalue chaque coup puis undo).
- Tests : tests pour Board, Rules, Heuristic et intégration AI (pytest).
- Logs : la console affiche des logs de diagnostic (valid moves, score évalué pour heuristique).

Arborescence
- src/board.py
- src/rules.py
- src/heuristic.py
- src/ai.py
- src/cli.py
- tests/test_board.py
- tests/test_rules.py
- tests/test_heuristic.py
- tests/test_ai_integration.py
- docs/

Installation
1. Ouvrir le projet:
   cd C:\Users\cloeh\jeu-puissance4
2. Activer l’environnement:
   .venv\Scripts\Activate
3. Installer dépendances:
   python -m pip install -U pip
   python -m pip install pytest

Exécution des tests
- Lancer tous les tests :
  python -m pytest -q
- Résultat attendu : tests verts.

Lancer la boucle console
- Démarrer une partie en console :
  python -m src.cli
- Choisir le mode :
  1) Human vs Random AI
  2) Human vs Heuristic AI
- Commandes :
  - entrer un numéro de colonne pour jouer
  - entrer q pour quitter
  - l’IA affiche: "AI debug: valid moves = [...]" puis "AI chosen (...) -> col N [with score S]"

Notes d’implémentation
- Heuristique : analyse toutes les fenêtres de longueur 4 (horizontales, verticales, diagonales), applique des scores pour 4/3/2 en faveur ou contre, et renforce la présence au centre pour favoriser positions centrales.
- AI heuristique : simule chaque coup (drop), calcule heuristic(board, piece), puis undo pour restaurer l’état; choisit le coup au score le plus élevé.
- Règles : is_winning_move vérifie autour du dernier coup pour efficience.
- Stockage : grille par colonnes pour simplifier drop/undo.

Prochaines évolutions recommandées
- Intégrer la heuristique dans un Minimax + alpha‑beta pour une IA compétitive.
- Ajouter tests pour le CLI et couvrir cas limites (colonnes pleines, undo multiples).
- Ajouter logging vers fichier via module logging pour analyser parties.
- Ajouter fiche CONTRIBUTING.md et LICENSE.

Contribuer
- Fork le dépôt, créer une branche, écrire ou modifier des tests et ouvrir une PR.

Licence
- Ajouter un fichier LICENSE à la racine selon préférence (MIT, Apache 2.0, etc.).

# jeu-puissance4
Puissance 4 — projet majeure
