from estimateur import Estimateur
from somme import Somme

class Moyenne(Estimateur):
    ''''Permet de calculer la moyenne pondérée d'une variable numérique.

    Attributs
    ---------
    variable : Table
        Variable dont on veut calculer la somme. 
    
    Méthodes
    --------
    calcul(poids:list of int):
        Calcul la moyenne pondérée par la liste poids. Par défaut poids on donne un poids égal à chaque élément.

    Exemples
    --------
    >>>L=[1,2,3,4,5]
    >>>Moyenne.calcul(L)
    >>>3
    >>>poids=[0.5,0,0.1,0.1,0.3]
    >>>Moyenne.calcul(L,poids)
    >>>2.7
    '''
    
    def __init__(self, variable):
        self.variable=variable
    
    def calcul(self, poids=None):
        '''Calcule la moyenne pondérée d'une variable numérique.
        
        Paramètres
        ----------
        poids(list of int):
            Le poids associé à chaque observation. Par défaut on donne un poids égal à chaque observation.
            
        Retourne
        --------
        S : int
            La moyenne pondérée
        Error : 
            Un message d'erreur, si les poids ne sont pas de somme 1
            
        Exemples
        --------
        >>>L=[1,2,3,4,5]
        >>>Moyenne.calcul(L)
        >>>3
        >>>poids=[0.5,0,0.1,0.1,0.3]
        >>>Moyenne.calcul(L,poids)
        >>>2.7
        '''
        if not(poids):
            poids=[1/len(self.variable)]*len(self.variable)
        S=0
        if not(Somme.calcul(poids)==1):
            raise Exception("Attention! La somme des poids n'est pas égale à 1.")
        else:
            for i in range(len(self.variable)):
                S+=poids[i]*self.variable[i]
            return S


