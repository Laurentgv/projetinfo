from outils import Outils
from Table import Table

class Transforme(Table):
    '''Cette classe permet de transformer les données importees dans un format : liste de listes
    
    Attributs
    ---------
    data:
        Les données importées qui sont dans un format spécifique à la fonction d'importation.
        
    Méthodes
    --------
    json_data(file:list of dict):list of list
        Fonction qui transforme une liste de dictionnaire de la forme : ['nom':'...', 'id':'...', 'données':dict, 'time':'...']
        en une liste de liste de la forme : data[ligne][colonne]=data[individu][variable].

    Exemples
    --------
    >>>
    >>>
    >>>
    >>>
    '''

    def __init__(self, file) -> None:
        self.file=file
    
    def json_data(self):
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
        for i in range(len(self.file)):
            tete=Outils.fusion(tete, Outils.clef_dict_imbrique(self.file[i], [])[0])
            clef_passage = Outils.fusion(clef_passage, Outils.clef_dict_imbrique(self.file[i], [])[1])

        #Cree le tableau de la bonne dimension de none
        data=[[None for x in range(len(tete))] for x in range(len(self.file))]

        #On titre les colonnes
        for i in range(len(tete)):
            data[0][i]=tete[i]

        #On remplit d'abord les données issues des sous-dictionnaires
        for i in range(len(self.file)):
            for j in clef_passage:
                sous_clef=Outils.clefs_dictionnaire(self.file[i][j])
                for k in sous_clef:
                    data[i][tete.index(k)]=self.file[i][j][k]

        #On remplit les données issues du dictionnaire principale
        for i in range(len(self.file)):
            for j in range(len(tete)):
                if (tete[j] in Outils.clefs_dictionnaire(self.file[i])) and not(tete[j] in clef_passage):
                    data[i][j]=self.file[i][tete[j]]

        return (data)



