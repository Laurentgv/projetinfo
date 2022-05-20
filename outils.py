def fusion(L1, L2):
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