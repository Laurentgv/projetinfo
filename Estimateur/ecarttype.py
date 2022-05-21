from estimateur import Estimateur
from moyenne import Moyenne
import numpy as np

class EcartType(Estimateur):
    '''Permet de calculer l'écart-type d'une variable numérique.

    Attributes
    ---------
    variable : list of int
        Variabe numerique dont on veut calculer l'ecart-type.
    

    Examples
    --------
    >>>L=[1,2,3,4,5]
    >>>EcartType.calcul(L)
    >>>1.58
    '''

    def __init__(self, variable):
        self.variable=variable

    def calcul(self):
        '''Calcul l'ecart-type d'une variable numerique.
        
        Parameters
        ----------
       
        Returns
        --------
        s : int 
            L'ecart-type de la variable. Attention, on calcul l'ecart-type avec la variance empirique est ce la bonne méthode ?
        
        Examples
        --------
        >>>L=[1,2,3,4,5]
        >>>EcartType.calcul(L)
        >>>1.58
        '''
        M=Moyenne.calcul(self.variable)
        S=0
        c=0
        for i in range(len(self.variable)):
            if not(self.variable[i]):
                c+=1
            else:
                S+=((self.variable[i]-M)**2)
        V=S*(1/(len(self.variable)-1))
        if not(c==0):
            print('Attention, l écart-type qui vient d être calculé comporte '+str(c)+' valeurs manquantes')
        return np.sqrt(V)
