🧮 Le Compte Est Bon - Jeu en Python

Ce programme permet à l’utilisateur de jouer à une version numérique du célèbre jeu télévisé "Le Compte est Bon". Le but est simple : à partir de 6 nombres tirés au hasard, et en utilisant les quatre opérations mathématiques de base, il faut se rapprocher le plus possible d’un nombre cible (entre 101 et 999).

🎮 Règles du jeu

Le programme tire au hasard :

Un nombre cible à atteindre, entre 101 et 999.

6 plaques numérotées, tirées parmi un ensemble de 24 plaques réparties comme suit :

Chaque nombre de 1 à 10 est présent 2 fois.

Les nombres 25, 50, 75, 100 sont présents 1 seule fois.

À chaque tour :

L’utilisateur choisit une opération : addition (+), soustraction (−), multiplication (×) ou division (÷).

Il sélectionne deux nombres parmi ceux disponibles (plaques restantes ou résultats précédents).

Le résultat de l’opération est ajouté à la liste des nombres disponibles, et les deux nombres utilisés sont retirés.

Le jeu continue jusqu’à :

Ce qu’il ne reste qu’un seul nombre.

Ou que l’utilisateur choisisse de terminer la partie.

À la fin, le programme indique :

Si le compte est bon (c’est-à-dire si le nombre cible a été atteint).

Sinon, il affiche le meilleur résultat obtenu (le plus proche du nombre cible).