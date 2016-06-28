# coding: latin-1
import quicksort2

# construction de l'arbre
racine = quicksort2.construit_arbre ()
# construction de l'image du graphe
racine.image ("graph.txt", "graph.png")

# cr�ation d'un fichier HTML
f = open ("page.html", "w")
f.write ("<body><html>\n")              # d�but

f.write ("<H1> liste tri�e </H1>\n")    # titre pour la liste tri�e
s = str (racine)                        # on r�cup�re la liste tri�e
s = s.replace ("\n", "<BR>\n")          # <BR> permet de passer � la ligne
f.write (s)

f.write ("<H1> graphe </H1>\n")         # titre pour l'image
f.write ('<img src="graph.png" width=400/>\n')    # image

f.write ("<H1> code du graphe </H1>\n") # titre pour le code du graphe
s = racine.chaine_graphe ()             # on r�cup�re le code du graphe
f.write ("<pre>\n")                     # on l'affiche tel quel
f.write (s)
f.write ("</pre>\n")

f.write ("</html></body>\n")            # fin
f.close ()

# on lance le navigateur automatiquement pour afficher la page
import os
os.system (r'"C:\Program Files\Mozilla Firefox\firefox" page.html')