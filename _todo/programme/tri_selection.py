# coding: cp1252
import random

def construit_suite(n):
    """construit une liste de n nombres entiers compris entre 0 et 99"""
    l = []
    for i in range(0,n):
        l.append (random.randint(0,100))
    return l

def tri_selection(l):
    """ tri une liste l, tri par s�lection"""
    # premi�re boucle, r�p�tition des �tapes A et B
    for i in range(0,len(l)):

        # recherche du maximum, on suppose pour commencer
        # qu'il est � la position 0
        pos = 0
        # boucle de l'�tape A
        for j in range(1,len(l)-i):
            if l [pos] < l [j]: pos = j

        # �change de l'�tape B
        # la position du maximum est conserv� dans la variable pos
        # on fait l'�change avec l'�l�ment � la position len(l)-i-1
        k       = len(l)-i-1
        ech     = l [k]
        l [k]   = l [pos]
        l [pos] = ech

l = construit_suite(8)          # cr�ation d'une suite al�atoirement
print "liste non tri�e :\t",l   # affichage
tri_selection (l)               # tri
print "liste tri�e     :\t",l   # affichage
