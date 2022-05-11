from estimateur import Estimateur
from moyenne import Moyenne
import numpy as np

class EcartType(Estimateur):
    '''Un estimateur, l'écart type
    '''

    def __init__(self, variable):
        self.variable=variable

    def calcul(self):
        M=Moyenne.calcul(self.variable)
        S=0
        for i in range(len(self.variable)):
            S+=((self.variable[i]-M)**2)
        V=S*(1/(len(self.variable)-1))
        return np.sqrt(V)