from estimateur.estimateur import Estimateur
from table.table import Table
from estimateur.moyenne import Moyenne

class Covariance(Estimateur):

    def __init__(self, variable) -> None:
        self.variable=variable

    def calcul(self, variable):
        n=len(variable)
        X=Moyenne(self.variable).calcul()
        Y=Moyenne(variable).calcul()
        C=0
        for i in range(n):    
            C+=(self.variable[i])*(variable[i])
        C=C/n
        return C-X*Y