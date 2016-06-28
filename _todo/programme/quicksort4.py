# coding: latin-1
import quicksort2

# construction de l'arbre
racine = quicksort2.construit_arbre ()
# construction de l'image du graphe
racine.image ("graph.txt", "graph.png")

# construction du d�but du fichier tex
package = """a4 amsmath amssymb subfigure float latexsym amsfonts
epic eepic makeidx multido varindex moreverb alltt fancyvrb fancyhdr
color eurosym tabularx placeins url shorttoc""".split ()

header = """\\documentclass[french,11pt]{article}\n\\usepackage[french]{babel}
\\usepackage[usenames]{color}\\usepackage{""" + \
                          "}\n\\usepackage{".join (package) + \
"""}\\usepackage[small,normal]{caption2}\\urlstyle{sf}
\\usepackage[pdftex]{graphicx}\usepackage[T1]{fontenc}
\DefineVerbatimEnvironment{verbatimx}{Verbatim}{frame=single, 
framerule=.1pt, framesep=1.5mm, fontsize=\\footnotesize,xleftmargin=0pt}
\\begin{document}\n"""

# cr�ation d'un fichier tex
f = open ("page.tex", "w")
f.write (header)

f.write ("\\title{Tri quicksort}\n")    # d�finit le titre
f.write ("\\maketitle\n")               # �crit le titre
f.write ("\\tableofcontents\n")         # table des mati�res

f.write ("\\section{liste tri�e}\n")    # titre pour la liste tri�e
s = str (racine)                        # on r�cup�re la liste tri�e
s = s.replace ("\n", "\\\\  \n")        # \\ passe � la ligne
f.write ("\\begin{tabular}{|l|}\n")
f.write (s)
f.write ("\\end{tabular}\n")

f.write ("\\section{graphe}\n")         # titre pour l'image
f.write ('\\includegraphics[height=5cm]{graph.png}\n')    # image

f.write ("\\section{code du graphe}\n") # titre pour le code du graphe
s = racine.chaine_graphe ()             # on r�cup�re le code du graphe
f.write ("\\begin{verbatimx}\n")        # on l'affiche tel quel
f.write (s)
f.write ("\\end{verbatimx}\n")

f.write ("\\end{document}\n")            # fin
f.close ()

# on compile deux fois le fichier pour que la table des mati�res
# soit bien prise en compte
import os
os.system (r'"C:\Program Files\MiKTeX 2.7\miktex\bin\pdflatex" page.tex')
os.system (r'"C:\Program Files\MiKTeX 2.7\miktex\bin\pdflatex" page.tex')

# on affiche le r�sultat avec Adobe Reader
os.system (r'"C:\Program Files\Adobe\Reader 9.0\Reader\AcroRd32.exe" page.pdf')