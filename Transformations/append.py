from table.Table import Table
from transformations.transformation import Transformations
import outils

class Append(Transformations):
    '''On ajoute des individus'''

    def __init__(self):
        '''
        Constructeur
        '''
        pass

    def transfo(table1:Table, table2:Table):
        #Création d'un tableau de la dimension finale de 'None'
        sortie=[[None for x in range(len(outils.fusion(table1.var, table2.var))) ] for x in range(len(table1.data)+len(table2.data)-1)]
        #On rempli tout de suite la première ligne avec le nom des colonnes
        variables=outils.fusion(table1.var, table2.var)

        #On remplit le tableau sortie avec les données de self.data
        for i in range(len(table1.data)):
            for j in range(len(table1.var)):
                sortie[i][j]=table1.data[i][j]

        #On remplit le tableau sortie avec les données de data_fille
        for i in range(len(table1.data), len(table1.data)+len(table2.data)-1):
                for k in range(len(table2.var)):
                    sortie[i][variables.index(table2.var[k])]=table2.data[i-len(table1.data)+1][table2.var.index(table2.var[k])]
       
        return Table(variables, sortie)