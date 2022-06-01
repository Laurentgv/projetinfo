import matplotlib.pyplot as plt
from table.table import Table
from estimateur.reglin import Reglin
import numpy as np

class Plot():
    def __init__(self, table) -> None:
        self.table=table

    def scatterplot(self, table, titre):
        plt.scatter(self.table.data, table.data)
        plt.title(titre)
        plt.xlabel(self.table.var[0])
        plt.ylabel(table.var[0])
        return plt.show()
    
    def scatlinreg(self, table, titre):
        plt.scatter(self.table.data, table.data)
        plt.title(titre)
        plt.xlabel(self.table.var[0])
        plt.ylabel(table.var[0])
        beta0, beta1, Rcarre = Reglin(self.table.data).calcul(table.data)
        def f(x):
            return beta1*x+beta0
        x = np.linspace(int(min(self.table.data))-5, int(max(self.table.data))+5, 100)
        plt.plot(x, f(x), color="red")
        plt.plot(x, f(x), color="red", label="R-carré = "+str(Rcarre))
        plt.legend(loc="upper right")
        return plt.show()
