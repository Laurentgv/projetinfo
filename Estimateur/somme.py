from estimateur import Estimateur

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
    >>>L=[1,2,3,4,5]
    >>>Somme.calcul(L)
    >>>15
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
        >>>L=[1,2,3,4,5]
        >>>Somme.calcul(L)
        >>>3
        '''
        S=0
        for i in range(len(self.variable)):
            S+=self.variable[i]
        return S
