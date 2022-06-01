from table.table import Table
from transformations.transformation import Transformations
import outils

class Mapping(Transformations):

    def __init__(self):
        super().__init__()
    
    def transfo(table1, valeur1, table2, valeur2, valeur3):
        L=[]
        for i in range(len(table1.data)):
            X=table1.data[i][table1.var.index(valeur1)]
            T=outils.velookup(table2, valeur2, valeur3, X)
            L.append(T)
        return Table.ajouter_var(table1, valeur3, L)

#test1=Table(['map', 'numero'],[[2012, 456], [2014, 345], [2013,678]])
#test2=Table(['mapping', 'café', 'instrument'], [[2012, 0, 12], [2014, 1, 567], [2013, 1, 5678]])
#what=Mapping.transfo(test1, 'map', test2, 'mapping', 'café')