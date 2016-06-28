# coding: cp1252
import random

def construit_suite(n):
    """construit une liste de n nombres entiers compris entre 0 et 99"""
    l = []
    for i in range(0,n):
        l.append (random.randint(0,100))
    return l

def fusion_liste (l1,l2):
    """fusionne deux listes l1 et l2 tri�es par ordre croissant
    de sorte que la liste r�sultante soit �galement tri�e"""
    i,j,k = 0,0,0
    fin   = len (l1) + len (l2)
    l = []
    while k < fin :
        if j >= len (l2) or (i < len (l1) and l1 [i] < l2 [j]) :
            l.append (l1 [i])
            k += 1
            i += 1
        else :
            l.append (l2 [j])
            k += 1
            j += 1
    return l

def tri_fusion(l):
    """ tri une liste l par fusion"""
    if len (l) <= 1 : return None # on �limine le cas simple
    n = 1
    while n < len (l) :
        for i in xrange (0, len (l), 2*n):
            a  = i
            m  = min (len (l), a + n)
            b  = min (len (l), a + 2 * n)
            if m < b:
                t        = fusion_liste (l [a:m], l [m:b])
                l [a:b] = t
        n *= 2
        
l = construit_suite(13)          # cr�ation d'une suite al�atoirement
print l [0:3]
print "liste non tri�e :\t",l    # affichage
tri_fusion (l)                   # tri
print "liste tri�e     :\t",l    # affichage
