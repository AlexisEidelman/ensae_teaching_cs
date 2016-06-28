# coding: cp1252
import random                 # pour tirer al�atoirement des nombres
import math                   # fonction sqrt
import PIL.Image as Im        # pour les images
import PIL.ImageDraw as Id    # pour dessiner

infini = 10000000 # l'infini est �gal � dix millions, c'est une variable globale

def construit_ville(n, x =1000, y = 800):
    """tire al�atoirement n villes dans un carr�e x * y, on choisit
    ces villes de sortent qu'elles ne soient pas trop proches"""
    # deux villes ne pourront pas �tre plus proches que mind
    mind = math.sqrt (x*x+y*y) / (n * 0.75)
    # liste vide
    l = []
    while n > 0:
        # on tire al�atoirement les coordonn�es d'une ville
        xx = x * random.random ()
        yy = y * random.random ()
        # on v�rifie qu'elle n'est pas trop proche d'aucune autre ville
        ajout = True
        for t in l :
            d1 = t [0] - xx
            d2 = t [1] - yy
            d  = math.sqrt (d1*d1+d2*d2)
            if d < mind :
                ajout = False  # ville trop proche
        # si la ville n'est pas trop proche des autres, on l'ajoute � la liste
        if ajout:
            l.append ((xx,yy))
            n -= 1  # une ville en moins � choisir
    return l

def distance_ville (l,i,j):
    """calcule la distance entre deux villes i et j de la liste l"""
    x = l [i][0] - l [j][0]
    y = l [i][1] - l [j][1]
    return math.sqrt (float (x*x+y*y))

def construit_arete (l,part = 0.15):
    """tire al�atoirement part * len (l) ar�tes et construit la matrice
    d'adjacence"""
    global infini
    nb  = len (l)
    m   = [ [ 0 for i in range(0,nb) ] for i in range (0,nb) ] # cr�e un vecteur de nb z�ros

    are = int (part * nb * nb)
    while are > 0:
        i = random.randint (0,nb-1)            # premi�re ville
        j = random.randint (0,nb-1)            # seconde ville
        if i == j : continue                   # pas besoin d'ar�te entre i et i
        if m [i][j] > 0: continue               # si l'ar�te existe d�j�, on recommence
        m [i][j] = int (distance_ville (l,i,j)) # on affecte comme poids � l'ar�te
                                                # la distance entre les deux villes
        m [j][i] = m [i][j] # sym�trie de la matrice car le graphe est non orient�
        are -= 2            # deux cases de la matrice ne sont plus nulles

    # on associe � toutes les ar�tes nulles de poids nul, donc inexistantes,
    # une valeur �gale � l'infini pour signifier qu'elles ne sont pas reli�es
    global infini
    for i in range (0, nb):
        for j in range (0, nb):
            if m [i][j] == 0:
                m [i][j] = infini

    return m

def dessin_ville_arete (l,m,chemin):
    """dessine la ville et les routes dans une image"""

    # on prend les coordonn�es maximales
    mx, my = 0,0
    for i in l:
        mx = max (mx, i [0])
        my = max (my, i [1])
    mx += 25
    my += 25
    mx, my = int (mx), int (my)
    im = Im.new ("RGB", (mx, my), (255,255,255)) # cr�ation d'une image blanche
    draw = Id.Draw(im)

    # dessin des villes
    for i in l:
        j  = (int (i [0]), int (i[1]))
        j2 = (j [0] + 10, j [1] + 10)
        draw.ellipse ((j,j2), fill = (0,0,0))

    # dessin des ar�tes
    global infini
    for i in range (0,len(l)):
        for j in range (0,len(l)):
            if m [i][j] > 0 and m [i][j] < infini :
                a = (int (l [i][0]+5), int (l [i][1]+5))
                b = (int (l [j][0]+5), int (l [j][1]+5))
                draw.line ((a,b),fill=(255,0,0))

    # dessin des villes de d�part et d'arriv�e en vert
    v1 = chemin [0]
    v2 = chemin [ len (chemin)-1]
    a = (int (l [v1][0]), int (l [v1][1]))
    b = (int (l [v1][0]+10), int (l [v1][1]+10))
    draw.ellipse ((a,b), fill = (0,255,0))
    a = (int (l [v2][0]), int (l [v2][1]))
    b = (int (l [v2][0]+10), int (l [v2][1]+10))
    draw.ellipse ((a,b), fill = (0,255,0))

    # dessin du chemin, ar�tes en bleu
    for c in range (0,len(chemin)-1):
        i = chemin [c]
        j = chemin [c+1]
        if m [i][j] > 0 and m [i][j] < infini :
            a = (int (l [i][0]+5), int (l [i][1]+5))
            b = (int (l [j][0]+5), int (l [j][1]+5))
            draw.line ((a,b),fill=(0,0,255))
        else:
            a = (int (l [i][0]+5), int (l [i][1]+5))
            b = (int (l [j][0]+5), int (l [j][1]+5))
            draw.line ((a,b),fill=(0,0,50))

    # on retourne l'image
    return im

def meilleur_chemin (n,m,a,b):
    """d�termine le meilleur chemin,
    n est le nombre de villes,
    m est la matrice d'adjacence,
    a est la ville de d�part,
    b la ville d'arriv�e"""

    # cr�ation d'un tableau, d [i] contient la meilleure distance minimale actuelle
    # s�parant la ville i de la ville a
    d = [ 10000000 for i in range(0,n) ]

    # p [i] contient la ville pr�d�cesseur qui permet d'atteindre la ville i
    # avec la distance d [i]
    p = [ -1 for i in range(0,n) ]

    # au d�part, seul la distance d[a] est nulle
    d [a] = 0

    # cette boucle s'ex�cute tant qu'on effectue des mises � jour
    # dans le tableau d[i]
    modif = 1
    while modif > 0:
        modif = 0
        # on parcourt toutes les ar�tes
        for i in range(0,n):
            for j in range (0,n):
                # nouvelle distance
                t = d [i] + m [i][j]
                if t < d [j] :  # si on a trouv� une meilleure distance minimale
                    d [j] = t   # on met � jour
                    p [j] = i
                    modif += 1  # une mise � jour de plus

    # on r�cup�re le meilleur chemin
    l = []
    while b != -1:
        l.append (b)
        b = p [b]
    # on le retourne
    l.reverse ()
    return l

def choix_villes_depart_arrive(nb,m):
    """cette fonction choisit deux villes al�atoirement, d�part et arriv�e,
    elle �vite que la ville et d�part et d'arriv�e soient les m�mes,
    elle �vite que ces deux villes soient reli�s par un seul arc,
    elle choisit deux villes pour lesquelles il existe un meilleur
    chemin"""
    global infini
    a,b = -1,-1
    tour = 0
    while True:
        a = random.randint (0,nb-1)     # premi�re ville au hasard
        b = random.randint (0,nb-1)     # seconde ville au hasard
        if a == b: continue             # villes identiques, on recommence
        if m [a][b] != infini : continue # villes reli�es, on recommence
        l = meilleur_chemin (nb,m,a,b)
        if l != None and len(l) > 3 :
            return a,b  # si le meilleur chemin existe,
                        # et n'est pas trop court (4 villes minimum,
                        # soit deux �tapes entre a et b), alors
                        # on retourne le r�sultat
        else:
            tour += 1
            if tour > 120 : return 0,0       # au bout de 120 essais, on s'arr�te

###############################################################################
# programme principal
# construction des villes
l = construit_ville (15)

# construction des ar�tes
print "adjacence"
m = construit_arete (l)

# choix de la ville de d�part de d'arriv�e
print "d�part"
a,b = choix_villes_depart_arrive(len(l),m)

print "recherche du meilleur chemin"
chemin  = meilleur_chemin (len(l), m, a,b)

if chemin != None and len(chemin) > 0:
    print "meilleur chemin ", a, " --> ", b, " : ", chemin
    # construction de l'image du r�sultat
    im = dessin_ville_arete(l,m,chemin)
    im.save ("image.png")
    im.show ()  # on affiche l'image
else :
    print "il n'existe pas de meilleur chemin"

