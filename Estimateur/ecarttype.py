from estimateur import Estimateur
from moyenne import Moyenne
import numpy as np

class EcartType(Estimateur):
    '''Permet de calculer l'écart-type d'une variable numérique.

    Attributs
    ---------
    variable : list of int
        Variabe numérique dont on veut calculer l'écart-type.
    
    Méthodes
    --------
    calcul():
        Calcul l'écrat-type de la variable.
    
    Exemples
    --------
    >>>L=[1,2,3,4,5]
    >>>EcartType.calcul(L)
    >>>1.58
    '''

    def __init__(self, variable):
        self.variable=variable

    def calcul(self):
        '''Calcul l'écart-type d'une variable numérique.
        
        Paramètres
        ----------
        Aucun
        
        Retourne
        --------
        s : int 
            L'écart-type de la variable. Attention, on calcul l'écart-type avec la variance empirique est ce la bonne méthode ?
        
        Exemples
        --------
        >>>L=[1,2,3,4,5]
        >>>EcartType.calcul(L)
        >>>1.58
        '''
        M=Moyenne.calcul(self.variable)
        S=0
        for i in range(len(self.variable)):
            S+=((self.variable[i]-M)**2)
        V=S*(1/(len(self.variable)-1))
        return np.sqrt(V)