# coding: cp1252
# la premi�re ligne permet d'ins�rer des accents dans les commentaires
import random
rejouer   = True
somme     = 0
nb_partie = 0
while rejouer :
    hasard     = rd.randint(1,20)
    nb_partie += 1

    devine = 0
    coup   = 0
    while devine != hasard :
        coup += 1
        devine = raw_input ("Entrer un nombre ?")
        devine = float (devine)     # conversion en r�el
        if (devine > hasard) :
            print "Le nombre entr� est trop grand."
        if (devine < hasard) :
            print "Le nombre entr� est trop petit."

    somme += coup
    print "Vous avez trouv� en " , coup, " coups."
    print "Vous avez d�j� jou� ", somme, " coups et ", nb_partie, " parties."
    rejouer = raw_input("Voulez-vous rejouer ?")
    rejouer = rejouer == "oui" or rejouer == "o" or rejouer == "1"

moyenne = float (somme) / nb_partie  # conversion en r�el, sinon la division est enti�re
print "Nombre de coups moyen par parties : " , moyenne