def pion_prendre(i,j,damier):
   c = damier [i][j]
   if c == 0: return False  # case vide, impossible de prendre
   c = 3 - c                # couleur de l'adversaire

   if damier [i-1][j-1] == c :     # s'il y a un pion adverse en haut � gauche
       if damier [i-2][j-2] == 0 : # si la case d'apr�s en diagonale est vide
           return True             # on peut prendre     

   # on r�p�te ce test pour les trois autres cases
   if damier [i-1][j+1] == c and damier [i-2][j+2] == 0: return True
   if damier [i+1][j-1] == c and damier [i+2][j-2] == 0: return True
   if damier [i+1][j+1] == c and damier [i+2][j+2] == 0: return True
        
   # si tous les tests ont �chou�, on ne peut pas prendre
   return False