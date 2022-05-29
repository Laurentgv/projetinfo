import outils
from table.Table import Table
from transformations.Agregation_spatiale import Agregation_spatiale

from estimateur.somme import Somme

#a=Table(["pays","temperature"],[["France",12],["UK",14],["US",14]])
#L2=a.l_index("temperature",14)
#print(L2)
#Table([pays],[[France],[UK]])

a=Table(['regions','superficie', 'latitude', 'temperature'],[['IdF',19,4523,28],['IdF',19,32149,14],['Normandie',43,12445,19],['Normandie',43,124133,21]])
#se=Agregation_spatiale(['temperature'],[],['latitude'],['superficie'],'regions')
#l=se.transfo(a)
#print(l.data)

s=Somme.calcul(a)
