# coding: cp1252
"""copie de fichiers sur une cl� USB, interface fen�tr�e"""

import Tkinter as Tk    # pour la fen�tre
import selection_file   # pour rechercher un r�pertoire
import copie_usb        # version sans fen�tre
import re               # pour les expressions r�guli�res

class copie_usb_window (copie_usb.copie_usb):
    """recopie des fichiers sur une cl� USB avec une fen�tre graphique"""
    
    def chercher (self, s, titre) :
        """modifie un r�pertoire"""
        fs = selection_file.FileSelection (titre, chemin = s, file = False)
        r  = fs.run ()
        if r != None : return r
        else : return s
            
    def fenetre (self) :
        """change les param�tres de la classe par l'interm�diaire d'une fen�tre"""
        
        # d�finition de la fen�tre
        root            = Tk.Tk ()

        source          = Tk.Entry (width = 100)
        source_label    = Tk.Label (text = "r�pertoire source")
        source_label.grid (column = 0, row = 0)
        source.grid (column = 1, row = 0)
        
        dest            = Tk.Entry (width = 100)
        dest_label      = Tk.Label (text = "r�pertoire destination")
        dest_label.grid (column = 0, row = 1)
        dest.grid (column = 1, row = 1)
        
        filtre_accept   = Tk.Entry (width = 100)
        accept_label    = Tk.Label (text = "filtre pour les fichiers accept�s")
        filtre_accept.grid (column = 1, row = 2)
        accept_label.grid (column = 0, row = 2)

        filtre_refuse   = Tk.Entry (width = 100)
        refuse_label    = Tk.Label (text = "filtre pour les fichiers refus�s")
        filtre_refuse.grid (column = 1, row = 3)
        refuse_label.grid (column = 0, row = 3)
        
        def chercher_source () : 
            s = source.get ()
            i = len (s)
            s = self.chercher (s, "r�pertoire source")
            source.delete (0, i)
            source.insert (0,s)
            
        def chercher_dest () :   
            s = dest.get ()
            i = len (s)
            s = self.chercher (s, "r�pertoire source")
            dest.delete (0, i)
            dest.insert (0,s)
        
        def copier () :   
            self.ch1    = source.get ()
            self.ch2    = dest.get ()
            self.accept = re.compile (filtre_accept.get ())
            self.refuse = re.compile (filtre_refuse.get ())
            self.copie ()
            
        brepsource      = Tk.Button (text = "chercher", command = chercher_source)
        brepdest        = Tk.Button (text = "chercher", command = chercher_dest)
        brepsource.grid (column = 2, row = 0)
        brepdest.grid (column = 2, row = 1)

        bfermer         = Tk.Button (text = "Fermer", command = root.destroy)
        bfermer.grid (column = 2, row = 4)
        bcopier         = Tk.Button (text = "Copier", command = copier)
        bcopier.grid (column = 2, row = 3)
        
        root.wm_title ("copie de fichiers vers une cl� USB")
        
        source.insert (0, self.ch1)
        dest.insert (0, self.ch2)
        filtre_accept.insert (0, self.accept.pattern)
        filtre_refuse.insert (0, self.refuse.pattern)
        
        root.mainloop ()
        
        
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
    
    c = copie_usb_window (ch1, ch2, filtre_accept, filtre_refuse)
    c.fenetre ()
    
    

