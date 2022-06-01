from table.Table import Table
from table.transforme import Transforme

from exporter.exporter import Exporter
from importer.importer import Importer

from estimateur.clustering import Clustering
from estimateur.ecarttype import EcartType
from estimateur.moyenne import Moyenne
from estimateur.somme import Somme

from transformations.Agregation_spatiale import Agregation_spatiale
from transformations.append import Append
from transformations.Centrage import Centrage
from transformations.Fenetrage import Fenetrage
from transformations.Jointure import Jointure
from transformations.Moyenne_glissante import Moyenne_glissante
from transformations.Normalisation import Normalisation
from transformations.Selection_de_variable import Selection_variable
from transformations.Transformations import Transformations

import meanbyvar
import outils

from table import Table

class Pipeline():
    '''
    '''
    def __init__(self):
        '''
        '''
        self.operations = []
    
    def ajout_etape(self,etape:Transformations):
        '''

        Parameters
        ----------
        etape : Transformations
            opération ajoutée à la pipeline
        
        '''
        self.operations.append(etape)

    def run(self,table) -> Table :
        
        for etape in self.operations :
            table = etape(table).transfo()
        return table