from estimateur.moyenne import Moyenne
from table.table import Table
import time
from datetime import datetime

def fusion(L1:list, L2:list):
    '''Concatène deux listes en gardant leur ordre et en supprimant les doublons.
        
    Attributs
    ---------
    L1:
        Première liste à concatenner
            
    L2:
        Seconde liste à concatenner
            
    Retourne
    --------
    L1:
        La liste L1 à laquelle on a rajouté tous les éléments de L2 qui ne sont pas déjà dans L1, tout en gardant l'ordre de L1 et de L2.
            
    Exemples
    >>>
    >>>
    '''
    for i in L2:
        if not(i in L1):
            L1.append(i)
    return L1

    
def clefs_dictionnaire(dict):
    '''Renvoie la liste des clés d'un dictionnaire
        
    Attributs
    ---------
    dict:
        Dictionnaire dont on veut récuperer les clées
            
    Retourne
    --------
    L: 
        Liste contenant les clés de dict
            
    Exemples
    --------
    >>>
    >>>
    >>>
    '''
    L=[]
    for clef in dict.keys():
        L.append(clef)
    return L

    
def clef_dict_imbrique(data, clef_passage):
    '''Permet de récupérer toutes les clées d'un dictionnaire, même s'il y a plusieurs dictionnaire imbriqués.
        
    Attributs
    ---------
    data:
        Les données en dictionnaires
        
    clef_passage: 
        Une liste, qui doit être initilalisée à zéro par l'utilisateur. (idéalement attribut invisible à l'utilisateur)
        
    Retourne
    --------
    L1:
        Liste contenant toutes les clées de tous les dictionnaires imbriqués
        
    L2:
        Liste contenant les clées de data qui renvoient vers des dictionnaire.

    Exemples
    --------
    >>>
    >>>
    >>>
    '''
    clef=clefs_dictionnaire(data)
    sous_clef=[]
    for i in clef :
        if isinstance(data[i], dict):
            clef_passage.append(i)
            sous_clef=fusion(sous_clef, clef_dict_imbrique(data[i], clef_passage)[0])
    return (fusion(clef, sous_clef), clef_passage)

def type_date(table, variable, format):
    #pour csv format = '%Y%m%d%H%M%S.0' --- datetime.strptime('20130101000012.0', '%Y%m%d%H%M%S.0')
    #pour json date-heure format = '%Y-%m-%dT%H:%M:%S%z' --- datetime.strptime('2013-01-30T18:44:12+01:00', '%Y-%m-%dT%H:%M:%S%z')

    i = table.var.index(variable)
    table.var[i]='date'
    print(table.data)
    for j in range(len(table.data)):
        table.data[j][i]=datetime.strptime(str(table.data[j][i]), format)
    return table

def velookup(table, i, j, valeur):
    T=Table.extraire_var(table, i)
    if valeur in T.data:
        return Table.extraire_var(table, j).data[T.data.index(valeur)]
    else:
        return ("Pas trouvé")
