from estimateur.moyenne import Moyenne
from table.table import Table
from transformations.transformation import Transformations
import outils

class Meanbyvar(Transformations):

    def __init__(self) -> None:
        pass

    def transfo(table:Table, variable):
        variables=table.var
        donnee=table.data
        d=variables.index(variable)
        #on recupère la liste des differentes valeures
        L=[]
        for i in range(len(donnee)):
            outils.fusion(L, [donnee[i][d]])

        #On créé un tableau de none
        sortie=[[None for x in range(len(variables))] for x in range(len(L))]

        for valeur in L:
            intermediaire=[[None for x in range(len(variables))] for x in range(len(donnee))]
            for i in range(len(donnee)):
                if donnee[i][d]==valeur:
                    intermediaire[i]=donnee[i]
            for i in range(len(variables)):
                if i==d:
                    sortie[L.index(valeur)][i]=valeur
                else:
                    T=Table.extraire_var(Table(variables, intermediaire), variables[i])
                    sortie[L.index(valeur)][i]=Moyenne(T.data).calcul(None)
        return Table(variables, sortie)