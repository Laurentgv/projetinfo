class jointure():
    '''Permet de fusionner deux fichiers de données.
    Il faut pouvoir fusionner csv avec csv, json avec json, et peut être (?) csv avec json.

    Attributs
    ---------
    data : (list of list) or (list of dict)
        Table de données à laquelle on veut rajouter des données

    Méthodes
    --------
    fusion_csv(data_fille:list of list) : list of list
        Prend en argument une seconde table de variable et rajoute ses données à la table mère.

    fusion_json(data_fille:list of dict) : list of dict
        Prend en argument une table de données issue d'un fichier json et rajoute ses données à la table mère.

    Exemples
    --------
    >>>
    >>>
    '''

    def __init__(self, data) -> None:
        self.data=data
    
    def jointure_csv(self, data_fille:list):
        '''Fusionne deux tables de données issues de deux fichiers csv.
        
        Paramètres
        ----------
        data_fille : list of list
            Les données à rajouter, qui sont importer d'un fichier csv

        Retourne
        --------
        sortie : list of list
            Les deux tables concaténées, avec des None pour les valeurs manquantes.

        Exemples
        --------
        >>>data=[['nom1', 'nom2', 'nom3', 'nom4', 'nom5'], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        >>>data_fille=[['nom3', 'nom6', 'nom7'], [10, 20, 30], [10, 20, 30], [10, 20, 30], [10, 20, 30], [10, 20, 30]]
        >>>data.fusion_csv(data_fille)
        >>>[['nom1', 'nom2', 'nom3', 'nom4', 'nom5', 'nom6', 'nom7'], [1, 2, 3, 4, 5, None, None], [1, 2, 3, 4, 5, None, None], [1, 2, 3, 4, 5, None, None], [None, None, 10, None, None, 20, 30], [None, None, 10, None, None, 20, 30], [None, None, 10, None, None, 20, 30], [None, None, 10, None, None, 20, 30], [None, None, 10, None, None, 20, 30]]
        '''
        #Création d'un tableau de la dimension finale de 'None'
        sortie=[[None for x in range(len(list(set(self.data[0]+self.data_fille[0])))) ] for x in range(len(self.data)+len(data_fille)-1)]
        #On rempli tout de suite la première ligne avec le nom des colonnes
        sortie[0]=list(dict.fromkeys(self.data[0]+data_fille[0]))
        #On remplit le tableau sortie avec les données de self.data
        for i in range(len(self.data[0])):
            for j in range(len(self.data)):
                sortie[j][i]=(self.data[j][i])
        #On remplit le tableau sortie avec les données de data_fille
        for i in range(len(self.data), len(self.data)+len(data_fille)-1):
                for k in range(len(data_fille[0])):
                    sortie[i][sortie[0].index(data_fille[0][k])]=data_fille[i-len(self.data)+1][data_fille[0].index(data_fille[0][k])]
        return(sortie)

        
