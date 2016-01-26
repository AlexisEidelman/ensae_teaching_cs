

.. blogpost::
    :title: Numerical Recipes
    :keywords: Numerical Recipes, BLAS, LAPACK, Eigen, MKL, Intel MKL, Numpy
    :date: 2016-01-26
    :categories: calcul matriciel
    
    `numpy <http://www.numpy.org/>`_, 
    `scipy <http://www.scipy.org/>`_
    couvrent la plupart des besoins lorsqu'il s'agit de calcul
    matriciel. On ne se pose m�me plus la question de savoir comment
    c'est impl�ment�. Cette question revient lorsqu'on a besoin
    d'un algorithme en particulier et que celui-ci n'est pas 
    disponible dans l'environment dans lequel on programme.
    
    Il existe un livre c�l�bre qui reprend la plupart des besoins dans ce domaine :
    `numerical recipes <http://www2.units.it/ipl/students_area/imm2/files/Numerical_Recipes.pdf>`_,
    un petit millier de page de th�orie et de code. L'usage des code propos�s 
    est soumis � quelques `restrictions <https://fr.wikipedia.org/wiki/Numerical_Recipes#Critiques>`_
    et ils ne sont pas aussi rapides que les codes des librairies
    `BLAS <http://www.netlib.org/blas/>`_,
    `LAPACK <http://www.netlib.org/lapack/>`_,
    `LINPACK <http://www.netlib.org/linpack/>`_, 
    `ATLAS <http://math-atlas.sourceforge.net/>`_,
    `Eigen <http://eigen.tuxfamily.org/index.php?title=Main_Page>`_.
    
    Il y a aussi `Intel-MKL <https://software.intel.com/en-us/intel-mkl/>`_ 
    d�velopp�e par Intel qui explique le suffixe MKL ajout� � numpy 
    `numpy-mkl <https://software.intel.com/en-us/articles/numpyscipy-with-intel-mkl>`_.