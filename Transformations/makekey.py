from table.table import Table
from transformations.transformation import Transformations

class Makekey(Transformations):

    def __init__(self):
        super().__init__()

    def transfo(table, variable1, variable2):
        variables=table.var
        data=table.data
        #variables.append('clé_'+variable1+variable2)
        L=[]
        for i in range(len(data)):
            L.append((data[i][variables.index(variable1)], data[i][variables.index(variable2)]))
        return Table.ajouter_var(table, 'clé_'+variable1+variable2 , L)