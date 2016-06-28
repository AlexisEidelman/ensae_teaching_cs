# coding: cp1252
"""copie de fichiers sur une cl� USB, interface fen�tr�e, 
enregistrement des param�tres pr�c�dents"""

import copie_usb_window   # version avec fen�tre
import os.path            # pour d�tecter l'existence d'un fichier
import re                 # pour les expressions r�guli�res

class copie_usb_window_save (copie_usb_window.copie_usb_window):
    """recopie des fichiers sur une cl� USB avec une fen�tre graphique,
    et enregistrement des pr�c�dents param�tres"""

    def ecrire_parametre (self, txt) :
        """�criture des param�tres dans le fichier txt"""
        # ouverture du fichier en mode �criture
        f = open (txt, "w")
        f.write (self.ch1)
        f.write ("\n")
        f.write (self.ch2)
        f.write ("\n")
        f.write (self.accept.pattern)
        f.write ("\n")
        f.write (self.refuse.pattern)
        f.write ("\n")
        f.close ()
        
    def lire_parametre (self, txt) :
        """relecture des param�tres �crits dans le fichier txt s'il existe"""
        if os.path.exists (txt) :
            f           = open (txt, "r")
            
            s           = f.readline ()
            s = s.replace ("\n", "")
            self.ch1    = s
            
            s           = f.readline ()
            s = s.replace ("\n", "")
            self.ch2    = s
            
            s           = f.readline ()
            s = s.replace ("\n", "")
            self.accept = re.compile (s)
            
            s           = f.readline ()
            s = s.replace ("\n", "")
            self.refuse = re.compile (s)
            
            f.close ()

    def fenetre (self) :
        """m�thode fen�tre surcharg�e pour lire les derniers param�tres
        et enregistrer les nouveaux"""
        # premi�re �tape, lire les pr�c�dents param�tres
        self.lire_parametre ("copie_usb_window_save.txt")
        # seconde �tape, appel de la m�thode pr�c�dente
        copie_usb_window.copie_usb_window.fenetre (self) 
        # troisi�me �tape, �criture des param�tres
        self.ecrire_parametre ("copie_usb_window_save.txt")
        
        
if __name__ == "__main__" :
    
    print "copie de fichiers vers une cl� USB"
    ch1             = "C:\\Documents and Settings\\Dupr�\\" \
                        "Mes documents\\informatique\\support\\python_td"
    ch2             = "c:\\temp\\copie_usb"
    filtre_accept   = ".*[.].*"
    filtre_refuse   = ".*[.]pdf$|.*[.]html$|.*[.]bmp|programme\\\\.*[.]zip$"
    
    # filtre_accept accepte tout type de fichier
    # filtre_refuse refuse tous les fichiers dont l'extension est pdf, html ou 
    # inclus dans le r�pertoire programme et ayant l'extension zip
    
    c = copie_usb_window_save (ch1, ch2, filtre_accept, filtre_refuse)
    c.fenetre ()
    