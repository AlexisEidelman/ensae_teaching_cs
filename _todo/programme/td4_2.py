# coding: cp1252
import string

class SecondeInserstion (AttributeError):
    "insertion d'un mot d�j� ins�r�"

class NoeudTri :
    
    def __init__(self,s): self.mot = s
        
    def __str__(self):
        s = ""
        if "avant" in self.__dict__: s += self.avant.__str__ ()
        s += self.mot + "\n"
        if "apres" in self.__dict__: s += self.apres.__str__()
        return s
        
    def nouveau_noeud (self, s) :
        return NoeudTri (s)

    def insere (self,s):
        c = cmp (s, self.mot)
        if c == -1:
            if "avant" in self.__dict__ : self.avant.insere (s)
            else :  self.avant = self.nouveau_noeud (s)
        elif c == 1:
            if "apres" in self.__dict__ : self.apres.insere (s)
            else: self.apres = self.nouveau_noeud (s)
        else:
            raise SecondeInsertion, "mot : " + s
        
l = ["un", "deux", "unite", "dizaine", "exception", "dire", \
     "programme", "abc", "xyz", "opera", "quel"]
     
racine = None
for mot in l :
    if racine == None : racine = NoeudTri (mot)
    else : racine.insere (mot)

print racine