from estimateur.estimateur import Estimateur
from table.table import Table
from estimateur.ecarttype import EcartType
from estimateur.covariance import Covariance
from estimateur.moyenne import Moyenne

class Reglin(Estimateur):

    def __init__(self, variable):
        self.variable=variable

    def calcul(self, variable):
        P=EcartType(self.variable).calcul()*EcartType(self.variable).calcul()
        C=Covariance(self.variable).calcul(variable)
        beta1=C/P
        X=Moyenne(self.variable).calcul()
        Y=Moyenne(variable).calcul()
        beta0=Y-beta1*X
        return (beta0, beta1)