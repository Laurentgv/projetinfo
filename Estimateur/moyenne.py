from estimateur import Estimateur

class Moyenne(Estimateur):
    ''''
    Un estimateur, la moyenne, dont le but est de calculer la moyenne d'une variable.
    '''
    
    def __init__(self, variable):
        self.variable=variable
    
    def calcul(self, poids=[1/len(self.variable)]*len(self.variable)):
        '''Calcul de la moyenne avec des poids'''
        S=0
        for i in range(len(self.variable)):
            S=poids[i]*self.variable[i]
        return S/len(self.variable)

