from table import Table
import outils

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

    def __init__(self) -> None:
    
    def json_data(self, file):
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
        data=[[None for x in range(len(tete))] for x in range(len(file))]

        #On titre les colonnes
        for i in range(len(tete)):
            data[0][i]=tete[i]

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

        return (data)



