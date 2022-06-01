from estimateur.estimateur import Estimateur
from table.table import Table

class Somme(Estimateur):
    '''Permet de calculer la somme d'une variable numérique

    Attributs
    ---------
    variable : list of int
        Variable dont on veut calculer la somme. 

    
    Méthode
    -------
    calcul():
        Permet de calculer la somme de la variable.

    Exemples
    --------

    '''

    def __init__(self, variable):
        self.variable=variable

    def calcul(self):
        '''Calcul la somme d'une variable numérique.
        
        Paramètre
        ---------
        Aucun
        
        Retourne
        --------
        S : int
        
        Exemples
        -------

        '''
        S=0
        m=0
        for i in range(len(self.variable)):
            if not(self.variable[i]):
                m+=1
            else:
                S+=self.variable[i]
        if not(m==0):
            print('Attention, la somme qui vient d être calculée comporte ' +str(m)+' valeurs manquantes')
        return S
