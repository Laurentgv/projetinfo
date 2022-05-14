from abc import ABC, abstractmethod

class Importer(ABC):
    '''Classe abstraite pour differencier l'import .csv et l'import .json
    '''
    def __init__(self) -> None:
        super().__init__()
