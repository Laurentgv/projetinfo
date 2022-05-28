from estimateur.estimateur import Estimateur
from estimateur.somme import Somme

class Moyenne(Estimateur):
    ''''Permet de calculer la moyenne pondérée d'une variable numérique.

    Attributs
    ---------
    variable : list of int
        Variable dont on veut calculer la somme. 
    
    Méthodes
    --------
    calcul(poids:list of int):
        Calcul la moyenne pondérée par la liste poids. Par défaut poids on donne un poids égal à chaque élément.

    Exemples
    --------
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
        '''
        print(self.variable)
        if not(poids):
            poids=[1/len(self.variable)]*len(self.variable)
        S=0
        m=0
        if not(round(Somme(poids).calcul())==1):
            raise Exception("Attention! La somme des poids n'est pas égale à 1.")
        else:
            for i in range(len(self.variable)):
                if not(self.variable[i]):
                    m+=1
                else:
                    S+=poids[i]*self.variable[i]
        if not(m==0):
            print('Attention, la moyenne qui vient d être calculée comporte '+str(m)+' valeurs manquantes')
        return S
