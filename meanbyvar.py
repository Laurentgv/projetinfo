from estimateur.moyenne import Moyenne
from table.Table import Table
from transformations.Transformations import Transformations
import outils

class meanbyvar(Transformations):

    def __init__(self) -> None:
        pass

    def transfo(table, variable):
        variables=table.var
        data=table.data
        d=variables.index(variable)
        #on recupère la liste des differentes valeures
        L=[]
        for i in range(len(data)):
            outils.fusion(L, [data[i][d]])
        
        #On créé un tableau de none
        sortie=[[None for x in range(len(variables))] for x in range(len(L))]

        for valeur in L:
            intermediaire=[[None for x in range(len(variables))] for x in range(len(data))]
            for i in range(len(data)):
                if data[i][d]==valeur:
                    intermediaire[i]=data[i]
            for i in range(len(variables)):
                T=Table(variables, intermediaire)
                sortie[L.index(valeur)][i]=Moyenne(Table.extraire_var(T, variables[i]))
        
        return Table(variables, L)

test=Table(['week', 'vitesse'], [[1, 50], [1, 100], [2, 10], [2, 20], [3, 5]])
meanbyvar.transfo(test, 'week')