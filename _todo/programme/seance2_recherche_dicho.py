# coding:latin-1
l = [2, 3, 6, 7, 9]
# si la liste n'est pas tri�e, il faut �crire : 
l.sort ()
x = 7

a = 0
b = len(l)-1
while a <= b :
    m = (a+b)//2  # ne pas oublier // sinon la division est r�elle
    if l[m] == x : 
        position = m   # ligne A
        break
    elif l[m] < x :
        a = m+1
    else :
        b = m-1

print ( position )

# si le nombre qu'on cherche x n'est pas dans la liste,
# le programme produit l'erreur suivante car la ligne A n'est jamais ex�cut�e :
"""
Traceback (most recent call last):
  File "seance2_recherche_dicho.py", line 19, in <module>
    print ( position )
NameError: name 'position' is not defined
"""
# soit n la longueur de la liste l
# le co�t d'une recherche simple est en O(n)
# le co�t d'une recherche dichotomique est en O(ln(n))