from estimateur.moyenne import Moyenne
from table.Table import Table
from transformations.Transformations import Transformations
import outils

class meanbyvar(Transformations):

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
                print("i="+str(i))
                if i==d:
                    sortie[L.index(valeur)][i]=donnee[L.index(valeur)][i]
                    print(donnee[L.index(valeur)][i])
                else:
                    T=Table.extraire_var(Table(variables, intermediaire), variables[i])
                    sortie[L.index(valeur)][i]=Moyenne(T).calcul(None)
                    print(T)
                    print("MOYENNE="+str(sortie[L.index(valeur)][i]))

            print(intermediaire)
        print(sortie)
        return Table(variables, sortie)

test=Table(['week', 'vitesse'], [[1, 50], [1, 100], [2, 10], [2, 20], [3, 5]])
meanbyvar.transfo(test, 'week')
Table.extraire_var(test,'vitesse')