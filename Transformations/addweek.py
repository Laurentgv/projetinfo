from table.table import Table
from transformations.transformation import Transformations
from datetime import datetime
import time

class Addweek(Transformations):
    def __init__(self):
        super().__init__()

    def transfo(table):
        d=table.var.index('date')
        table.var.append('week')
        for i in range(len(table.data)):
            table.data[i].append(table.data[i][d].isocalendar()[1])
        return table