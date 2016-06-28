# coding: cp1252
import random

def construit_suite(n):
    """construit une liste de n nombres entiers compris entre 0 et 99"""
    l = []
    for i in range(0,n):
        l.append (random.randint(0,100))
    return l

def recherche_dichotomique (l,x):
    """cherche l'�l�ment x dans la liste l, la liste l est
    suppos�e �tre tri�e par ordre croissant"""
    a = 0
    b = len(l)-1
    while a <= b :
        m = (a+b) // 2
        r = cmp (x, l[m])
        if r == 0 : return m
        elif r == -1 : b = m-1
        else : a = m + 1
    return a

def tri_insertion(l):
    """ tri une liste l par insertion dichotomique, on suppose que l est non vide"""
    lt = []
    for x in l :
        if len (lt) == 0 : 
            lt.append (x)
            continue
        m = recherche_dichotomique (lt, x)
        lt.insert (m, x)
    l [0:len (l)] = lt


l = construit_suite(13)         # cr�ation d'une suite al�atoirement
print l [0:3]
print "liste non tri�e :\t",l   # affichage
tri_insertion (l)               # tri
print "liste tri�e     :\t",l   # affichage
