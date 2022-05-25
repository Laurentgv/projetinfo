from Table import Table
import outils

class Transforme(Table):
    '''Cette classe permet de transformer les données importées dans un format : Table
    
    Attributs
    ---------
    data:
        Les données importées qui sont dans un format spécifique à la fonction d'importation.
        
    Méthodes
    --------
    transforme_json(file:list of dict):list of list
        Fonction qui transforme une liste de dictionnaire de la forme : ['nom':'...', 'id':'...', 'données':dict, 'time':'...']
        en une liste de liste de la forme : data[ligne][colonne]=data[individu][variable].

    transforme_csv(file:list of list, valeur_manquante:str):list of list
        Fonction qui prends les données csv importées en qui les renvoies au format Table avec des None pour les valeurs manquantes, et qui change le type des données en float.

    Exemples
    --------
    >>>
    >>>
    >>>
    >>>
    '''

    def __init__(Table):
        '''
        Constructeur

        '''
        super().__init__()
    
    def transforme_json(self, file):
        '''Permet de transformer une liste de dictionnaire de la forme : ['nom':'...', 'id':'...', 'données':dict, 'time':'...']
        en une liste de liste de la forme : data[ligne][colonne]=data[individu][variable]. 
        
        Attributs
        ---------
        
        Retourne
        --------
        data: 
            Les données issues du fichier json sous la forme d'une liste de liste de la forme : data[ligne][colonne]=data[individu][variable].
            
        Exemples
        --------
        >>>
         '''
        #Cree une liste des noms des variables
        tete=[]
        clef_passage=[]
        for i in range(len(file)):
            tete=outils.fusion(tete, outils.clef_dict_imbrique(file[i], [])[0])
            clef_passage = outils.fusion(clef_passage, outils.clef_dict_imbrique(file[i], [])[1])

        #Cree le tableau de la bonne dimension de none
        data=[[None for x in range(len(tete))] for x in range(len(file)-1)] # -1 dans le deuxième range due au format tuple du type Table.

        #On titre les colonnes
        variables=[]
        for i in range(len(tete)):
            variables.append(tete[i])

        #On remplit d'abord les données issues des sous-dictionnaires
        for i in range(len(file)):
            for j in clef_passage:
                sous_clef=outils.clefs_dictionnaire(file[i][j])
                for k in sous_clef:
                    data[i][tete.index(k)]=file[i][j][k]

        #On remplit les données issues du dictionnaire principale
        for i in range(len(file)):
            for j in range(len(tete)):
                if (tete[j] in outils.clefs_dictionnaire(file[i])) and not(tete[j] in clef_passage):
                    data[i][j]=file[i][tete[j]]

        return Table(variables, data)

    def transforme_csv(self, file, valeur_manquante):
        '''Permet de rendre opérationnel des données importées à partir d'un fichier csv.
        
        Attributs
        ---------
        file:
            Les données importées à partir d'un fichier csv.
        
        Retourne
        --------
        tuple:
            Les données issues du fichier csv sous le bon format. On a remplacer les valeurs manquantes par None, et changer les données numériques en type float.
        
        Exemples
        --------
        '''
        for i in range(1,len(file)):
            for j in range(len(file[0])):
                if file[i][j]==valeur_manquante:
                    file[i][j]=None
                else:
                    file[i][j]=float(file[i][j])
        
        return Table(file[0], file[1:])


    def transfo_format_date_json(self):
        '''
        Permet de changer le format de la date des donnees des fichiers en .json yyyy-mm-ddThh:mm:ss+01:00
        avec le format des fichiers en .csv yyyymmddhhmmss
        
        Attributes
        ----------
        Examples
        --------
        >>> a=Table([Région, date, Temperature],[[IdF, 2013-01-30T05:00:00+01:00, 23],[IdF, 2015-05-14T06:08:00+01:00, 13]])
        >>> a.transfo_format_date_json()
        >>> print(a.data)
        [[IdF, 20130130050000, 23],[IdF, 20150514060800, 13]]
        
        '''
        index=(self.var).index('date')
        donnees=self.data
        for i in range(len(self.data)):
            date=donnees[i][index]
            annee=str(date[0:4])
            mois=str(date[5:7])
            jour=str(date[8:10])
            heure=str(date[11::13])
            minute=str(date[14:16])
            seconde=str(date[17:19])
            donnees[i][index]=annee+mois+jour+heure+minute+seconde
            
            return Table(self.var,donnees)

