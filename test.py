from estimateur.ecarttype import EcartType
from estimateur.moyenne import Moyenne
from estimateur.somme import Somme
from importer.importer import Importer
from table.Table import Table
from table.transforme import Transforme
from estimateur.ecarttype import EcartType
from transformations.Normalisation import Normalisation
import time
from datetime import datetime
import outils

test_json=Importer.json_file("/Users/Louis/Downloads/données/données_électricité/2013-01.json.gz")

test_json2=Transforme.transforme_json(test_json)

test_json3=Transforme.type_date(test_json2, 'date_heure', '%Y-%m-%dT%H:%M:%S+01:00')

test_json4=Table.enlev_var(test_json3, 'date')
test_json4=Table.enlev_var(test_json3, 'record_timestamp')
test_json4=Table.enlev_var(test_json3, 'heure')
test_json4=Table.enlev_var(test_json3, 'statut_terega')
test_json4=Table.enlev_var(test_json3, 'statut_rte')
test_json4=Table.enlev_var(test_json3, 'statut_grtgaz')
test_json4=Table.enlev_var(test_json3, 'fields')
test_json4=Table.enlev_var(test_json3, 'recordid')

#Fenetrage should be working by now

janvier2013=Importer.json_file("/Users/Louis/Downloads/données/données_électricité/2013-01.json.gz")
fervier2013=Importer.json_file("/Users/Louis/Downloads/données/données_électricité/2013-02.json.gz")
mars2013=Importer.json_file("/Users/Louis/Downloads/données/données_électricité/2013-03.json.gz")
juillet2016=Importer.json_file("/Users/Louis/Downloads/données/données_électricité/2016-07.json.gz")

janvier2013_2=Transforme.transforme_json(janvier2013)
fevrier2013_2=Transforme.transforme_json(fervier2013)
mars2013_2=Transforme.transforme_json(mars2013)
juillet2013_2=Transforme.transforme_json(juillet2016)



Somme(test_json2.data[0]).calcul()
Moyenne(test_json2.data[0]).calcul(None)
EcartType(test_json2.data[0]).calcul()

test_csv=Importer.csv_file("/Users/Louis/Downloads/données/données_météo/synop.201301.csv.gz")
test_csv2=Transforme.transforme_csv(test_csv, 'mq')
test_csv3=Transforme.type_date(test_csv2, 'date', '%Y%m%d%H%M%S.0')
test_csv2.var
test_csv3.data

test_csv2.data[0]
print(test_csv2.data[0])
Somme(test_csv2.data[0]).calcul()
Moyenne(test_csv2.data[0]).calcul(None)
EcartType(test_csv2.data[0]).calcul()

#from transformations.Centrage import Centrage
#from transformations.Transformations import Transformations
test_csv=Importer.csv_file("/Users/Louis/Downloads/données/données_météo/synop.201301.csv.gz")
test_csv2=Transforme.transforme_csv(test_csv, 'mq')
Somme(test_csv2.data[0]).calcul()


#Centrage.transfo(test_csv2, 'dd')





test=Table(['week', 'vitesse'], [[1, 50], [1, 100], [2, 10], [2, 20], [3, 5]])
outils.toto(test, 'week')
