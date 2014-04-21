# -*- coding: utf8 -*-
"""
@file
@brief  quelques fonctions � propos de la premi�re s�ance
"""

def dix_entiers_carre():
    """
    fait la somme des dix premiers entiers au carr�
    
    :returns: nombre r�el
    
    @FAQ(Quelle est la diff�rence entre return et print ?)
    La fonction ``print`` sert � afficher un r�sultat sur la sortie standard.
    Elle peut �tre utilis�e � tout moment
    mais elle n'a pas d'impact sur le d�roulement programme. Le mot-cl� ``return``
    n'est utilis� que dans une fonction. Lorsque le programme rencontre
    une instruction commen�ant par ``return``, il quitte la fonction
    et transmet le r�sultat � l'instruction qui a appel� la fonction.
    @endFAQ
    
    @example(calcul de la somme des dix premiers entiers au carr�)
    Ce calcul simple peut s'�crire de diff�rentes mani�res.
    @code
    s = 0
    for i in range(1,11):
        s += i**2
    @endcode
    D'une fa�on abr�g�e :
    @code
    s = sum ( [ i**2 for i in range(1,11) ] )
    @endcode
    @endexample
    """
    s = 0
    for i in range(1,11):
        s += i**2
    return s