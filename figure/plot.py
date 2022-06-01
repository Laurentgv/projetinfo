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
        b, a = Reglin(self.table.data).calcul(table.data)
        seq=range(min(self.table.data), max(table.data))
        plt.plot(a*seq +b, color="r", lw=2.5)
        return plt.show()
