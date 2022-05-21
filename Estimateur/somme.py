from Estimateur.estimateur import Estimateur
from Table import Table

class Somme(Estimateur):
    '''Permet de calculer la somme d'une variable numérique

    Attributs
    ---------
    variable : list of int
        Variable dont on veut calculer la somme. 
        Attention, est ce que il faut prendre en compte le fait que la première ligne est le nom de la variable ?
        Les données sont aussi surement sous forme de liste de liste, est ce que il faut changer la méthode ou la classe dataframe va permettre de faire le job ?
    
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
