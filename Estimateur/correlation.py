from estimateur.estimateur import Estimateur
from table.table import Table
from estimateur.ecarttype import EcartType
from estimateur.covariance import Covariance

class Correlation(Estimateur):

    def __init__(self, variable):
        self.variable=variable

    def calcul(self, variable):
        P=EcartType(self.variable).calcul()*EcartType(variable).calcul()
        C=Covariance(self.variable).calcul(variable)
        return C/P