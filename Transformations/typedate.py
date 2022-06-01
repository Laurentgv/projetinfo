from table.table import Table
from transformations.transformation import Transformations
import time
from datetime import datetime

class Typedate(Transformations):

    def __init__(self):
        super().__init__()
    
    def transfo(table, variable, format):
    #pour csv format = '%Y%m%d%H%M%S.0' --- datetime.strptime('20130101000012.0', '%Y%m%d%H%M%S.0')
    #pour json date-heure format = '%Y-%m-%dT%H:%M:%S%z' --- datetime.strptime('2013-01-30T18:44:12+01:00', '%Y-%m-%dT%H:%M:%S%z')

        i = table.var.index(variable)
        table.var[i]='date'
        for j in range(len(table.data)):
            table.data[j][i]=datetime.strptime(str(table.data[j][i]), format)
        return table