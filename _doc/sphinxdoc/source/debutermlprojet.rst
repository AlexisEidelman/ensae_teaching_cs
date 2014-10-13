

.. _l-debutermlprojet:

Bien d�marrer un projet de machine learning
===========================================


Un projet de machine learning commence g�n�ralement avec un jeu de donn�es et un probl�me � r�soudre.
Une fois qu'on a cela, les premi�res �tapes d�butent avec presque toujours les m�mes questions :

Etape 1 : quel est le type de probl�me ?
++++++++++++++++++++++++++++++++++++++++

    * supervis� 
        * r�gression : :math:`Y = f(X) + \epsilon`
        * classification : :math:`(c_1,...,c_k) = f(X)` pour un probl�me � :math:`k` classes
        * ranking
    * non supervis�
        * clustering
        * r�duction du nombre de dimension
        * syst�me de recommandations
        
Etape 2 : quelles sont les donn�es ?
++++++++++++++++++++++++++++++++++++

    * Est-ce une table classique ou un graphe ?
    * Y a-t-il une dimension temporelle ?
    * Nombre d'observations ?
    * Nombre de variables (ou features) ?
    * Quelles sont les variables connues, les variables � pr�dire ?
    * Valeurs manquantes ?
    * Variables cat�gorielles, discr�tes ou continues ?
    
La plupart des algorithmes d'apprentissages utilisent des donn�es num�riques,
il faut convertir les variables cat�gorielles au format num�rique.

Si une variable cat�gorielle est � choix unique et qu'elle contient $C$ cat�gories, 
celle-ci sera multipli�e en $n$ colonnes, une pour chaque modalit�. Comme la somme de
ces colonnes est le vecteur colonne :math:`J=(1,...,1)`, la matrice :math:`X` modifi�e sera corr�l�e.
    
Etape 3 : s�paration train/test
+++++++++++++++++++++++++++++++

Il faut faire attention � deux ou trois d�tails. Par exemple, si le probl�me est un de probl�me 
de classification, il faut faire attention que toutes les classes � pr�dire sont bien repr�sent�es
dans les deux bases. C'est particuli�rement important si l'une d'elles comportent peu d'exemples.

Etape 4 : apprentissage d'un mod�le
+++++++++++++++++++++++++++++++++++

On cale un ou plusieurs mod�les sur les donn�es d'apprentissage.

Etape 5 : mesure de la performance
++++++++++++++++++++++++++++++++++

On mesure la performance du mod�le sur la base de test. Il existe certaines fa�ons standard de le faire en
fonction des types de probl�mes :

* classification
    * matrice de confusion
    * courbe ROC
    * pr�cision / rappel
* r�gression
    * erreur de pr�diction
* ranking
    * `DCG <http://en.wikipedia.org/wiki/Discounted_cumulative_gain>`_
    * `corr�lation de rang <http://en.wikipedia.org/wiki/Rank_correlation>`_
* clustering
    * variance intra classe, inter classe
    * nombre d'arc coup�s
* syst�me de recommandation
    * corr�lation de rang

Si la performance globale convient, on s'arr�te souvent ici. Dans le cas contraire, il faut retourner � l'�tape 4 :
    * La base d'apprentissage contient peut-�tre des points aberrants.
    * La distribution d'un variable n'est pas homog�ne dans les bases d'apprentissage et des tests.
    * Le mod�le a besoin de plus de variables :
        * combinaison non lin�aires des variables existantes (polyn�mes, fonctions en escalier, ...),
        * recoupement de la base de donn�es avec une autre base.
    * Les valeurs manquantes emp�chent le mod�le d'apprendre.
    * Une variables continues ne l'est pas vraiment : distribution selon deux modes par exemple.
    * ...
    
Voir �galement `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_.

Etape 6 : validation du mod�le
++++++++++++++++++++++++++++++

On regarde sur quelques exemples bien choisi que le mod�le proposent une r�ponse acceptables.
On applique des m�thodes du type validation crois�e.

