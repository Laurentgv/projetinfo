from abc import ABC, abstractmethod

class Estimateur(ABC):
    '''
    Metrique que l'on veut mesurer/étudier
    
    Je ne sais pas encore trop ce qu'il faut mettre dedans.
    '''
    def __init__(self) -> None:
        super().__init__()

    def calcul(self):
        return 0