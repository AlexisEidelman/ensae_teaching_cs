# coding: cp1252

import math
import random


def generate_expo(mu):
    return random.expovariate(mu)

S = 10000
iteration = 500
mu = 1.0 / 100

# cr�ation d'un tableau de S ampoule qui contient la dur�e de
# vide restante d'une ampoule
ampoule = [0 for a in range(0, S)]
moyenne_grille = 0
for i in range(0, iteration):
    grille = 0
    mean = 0
    for n in range(0, S):
        mean += ampoule[n]
        if ampoule[n] == 0:
            # remplacement d'une ampoule grill�e
            grille += 1
            # on d�termine la dur�e de vie de cette ampoule
            # on arrondit � l'entier le plus proche
            ampoule[n] = int(generate_expo(mu))
        else:
            # on enl�ve une heure � la dur�e de vie de l'ampoule
            ampoule[n] -= 1
    mean /= S
    if i > 0:
        moyenne_grille += grille
    print "it�ration : ", i, " moyenne dur�e : ", mean, " grill�es :", grille

moyenne_grille = float(moyenne_grille) / float(iteration - 1)
print "nombre moyen d'ampoules grill�es :", moyenne_grille
