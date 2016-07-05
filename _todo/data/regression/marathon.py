# coding:latin-1
import urllib
import os
import os.path


def charge_donnees():
    if os.path.exists("marathon.txt"):
        # si le fichier existe (il a d�j� �t� t�l�charg� une fois)
        f = open("marathon.txt", "r")
        text = f.read()
        f.close()
    else:
        # si le fichier n'existe pas
        link = "http://www.xavierdupre.fr/enseignement/complements/marathon.txt"
        url = urllib.urlopen(link)
        text = url.read()
        # on enregistre les donn�es pour �viter de les t�l�charger une seconde
        # fois
        f = open("marathon.txt", "w")
        f.write(text)
        f.close()

    lines = text.split("\n")
    lines = [l.split("\t") for l in lines if len(l) > 3]

    # conversion en r�el des donn�es num�rique
    for l in lines:
        l[1] = float(l[1])
        l[3] = float(l[3])
    return lines

if __name__ == "__main__":
    matrice = charge_donnees()
    print "nombre de lignes ", len(matrice)
