# Algorithmes et IA

Ce document décrit les algorithmes que nous avons utilisés dans le projet.

---

## Structures de données
- **Plateau (`Board`)** : matrice `grille[colonne][ligne]`.
- **Dernier coup** : stocké pour vérifier rapidement la victoire.
- **Fonctions principales** :
  - `sont_coup_valides()` : renvoie une liste avec les colonnes jouables
  - `jouer_coup()` / `annuler()` : permet la simulation de coups (sert pour nos ia)
  - `est_plein()` : permet de savoir si le plateau est rempli pour arreter le jeu

---

## IA aléatoire
- Choisit une colonne valide au hasard.
- Complexité : O(nb de colonnes).
- Utilité : elle nous a surtout aider au début pour que l'on puisse vérifier que le jeu sois jouable. Deplus elle était simple a coder.

---

## IA heuristique
- évalue toutes les cases du plateau grace a l'heuristique et renvoie le meilleur coup possible
Chaine étape décisionnelle
Heuristique :
- Analyse des fenêtres de 4 cases dans tous les sens .
- la pondération est choisi selon:
  - Nombre de pions du joueur/adversaire
  - Cases vides
  - Contrôle du centre (colonnes centrales favorisées)
- ajustement: Nous avons dû rajouter du "poids" au centre car sinon en début de partie l'ia suivait bien trop notre pion puisque nous étions les seules a impacter la notation du plateau. Nous avons aussi rajouter, avant notre heuristique des conditions de points s'il y a des coups gagnants ou perdants sur le plateau de facon a leur donner une importance primordiale.

---

## Minimax
- Exploration récursive de l’arbre des coups.
- **Maximizing player** : cherche a maximiser le score grace a la fonction `heuristic` .
- **Minimizing player** : cherche a minimiser le score grace a la fonction `heuristic` .
- Condition d’arrêt : victoire, match nul, profondeur atteinte.

---

## Choix des paramètres
- Profondeur : 
  - 5 actuellement pour une réponse plutot rapide mais elle peut etre modifié assez simplement (cf GAME.md).
  - attention cependant si l'on augmente le nb de lignes il faudra peut étre diminuer la profondeur car cela augmente considérablement la vitesse de réponse
- Scores : évaluer par la fonction `heuristic`.

## la classe board
comprend toutes les méthodes du plateau dont on se sert beaucoup dans le code
- chacunes a une déscription de ce qu'elle fait
- concernant la méthode str, elle nous a servi durant une grande partie du projet mais nous l'avons finalement délaisser pour nous tourner vers la fonction afficher_plateau car nous voulions pouvoir retourner un chemin gagnant en plus et que la méthode str ne pouvait pas prendre d'autre parametre comme un chemin. 

## heuristic.py
dans ce dossier il y a deux fonctions:
  - `score_window` qui prend en parametre une liste et un pion. elle va évaluer cette liste.
  - `heuristic` qui va évaluer toutes les cases du plateau en utilisant `score window` dans toutes les directions pour chacunes des cases.

## rules.py
  - `scan` permet de renvoyé le chemin gagnant s'il y en a un pour pouvoir ensuite l'afficher en dorée
  - `est_coup_gagnant` renvoie le chemin gagnant en utilisant `scan`
  - `est_match_nul` permet simplement de savoir s'il y a match nul