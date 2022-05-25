from abc import ABC, abstractmethod

class Estimateur(ABC):
    '''Classe abstraite des estimateurs.

    Attributs
    ---------

    Méthodes
    --------
    calcul : 
        Méthode abstraite

    Exemples
    --------
    '''
    def __init__(self) -> None:
        super().__init__()

    def calcul(self):
        '''Fonction qui permet d'effectuer le calcul de l'estimateur.
        Permet simplement de s'assurer que chaque classe d'estimateur possède bien une méthode calcul.
         
        Paramètres
        ----------
        Aucun
        
        Retourne
        --------
        Rien
        
        Exemples
        --------
        Aucun'''
        return None