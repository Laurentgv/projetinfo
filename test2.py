#import outils
from table.Table import Table
from transformations.Agregation_spatiale import Agregation_spatiale
#from transformations.Centrage import Centrage
#from transformations.Fenetrage import Fenetrage
#from transformations.Jointure import Jointure
#from transformations.Moyenne_glissante import Moyenne_glissante
#from transformations.Normalisation import Normalisation
#from transformations.Selection_de_variable import Selection_variable


a=Table(["pays","temperature"],[["France",12],["UK",14],["US",14]])
#L2=a.extraire_var("temperature")
#print(L2)
#Table([pays],[[France],[UK]])

a=Table(['region','superficie', 'latitude', 'temperature'],[['IdF',19,4523,28],['IdF',19,32149,14],['Normandie',43,12445,19],['Normandie',43,124133,21]])
se=Agregation_spatiale(['temperature'],[],['latitude'],['superficie'],'region')
l=se.transfo(a)
print(l.data)
#print(l.var)
#print(a.var)

#b=Centrage.transfo(a,'temperature')
#print(b.var)
#print(b.data)
