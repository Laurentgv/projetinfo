from estimateur.ecarttype import EcartType
from estimateur.moyenne import Moyenne
from estimateur.somme import Somme
from importer.importer import Importer
from table.Table import Table
from table.transforme import Transforme
from estimateur.ecarttype import EcartType
from transformations.Normalisation import Normalisation

test_json=Importer.json_file("/Users/Louis/Downloads/données/données_électricité/2013-01.json.gz")
print(test_json[-1])
print(len(test_json))
test_json2=Transforme.transforme_json(test_json)
print(len(test_json2.data[0]))
test_json3=Transforme.transfo_format_date_json(test_json2)


#datetime(*(time.strptime('2013-01-01T00:00:00+01:00', format)[0:6]))
#datetime(*(time.strptime('2013-01-01T00:00:00+01:00', '%Y%m%d %% %H%M%S %z')[0:6]))
#datetime.strptime(test_json3.data[0][7], '%Y%m%d %% %H%M%S')
datetime.fromisoformat(test_json3.data[0][7])
datetime.strptime(test_json3.data[0][5], '%Y%m%d')
import outils
import time
from datetime import datetime
test=type_date(test_json2, 'date', '%Y%m%d')
test=type_date(test_json2, 'heure', '%H%M%S')
datetime.strptime('18:00', '%H:%M')
datetime.strptime('2013-01-30T18:44:12+01:00', '%Y-%m-%dT%H:%M:%S%z')


print(test_json2.extraire_var('consommation_brute_gaz_terega'))

print(Normalisation(test_json2).transfo('consommation_brute_gaz_terega'))


datetime.strptime('20130101000012.0', '%Y%m%d%H%M%S.0')



Somme(test_json2.data[0]).calcul()
Moyenne(test_json2.data[0]).calcul(None)
EcartType(test_json2.data[0]).calcul()

test_csv=Importer.csv_file("/Users/Louis/Downloads/données/données_météo/synop.201301.csv.gz")
test_csv2=Transforme.transforme_csv(test_csv, 'mq', ['pmer', 'tend', 'cod_tend', 'dd', 'u', 'ww', 'w1', 'w2', 'nbas', 'hbas', 'cl', 'cm', 'ch', 'pres', 'niv_bar', 'geop', 'tend24', 'sw', 'etat_sol', 'nnuageN', 'ctypeN', 'hnuageN'], ['ff', 't', 'td', 'vv', 'n', 'tnN', 'txN', 'tminsol', 'tw', 'raf10', 'rafper', 'per', 'ht_neige', 'ssfrai', 'perssfrai', 'rrN', 'phenspeN'])
test_csv2.var
test_csv2.data

test_csv2.data[0]
print(test_csv2.data[0])
Somme(test_csv2.data[0]).calcul()
Moyenne(test_csv2.data[0]).calcul(None)
EcartType(test_csv2.data[0]).calcul()

#from transformations.Centrage import Centrage
#from transformations.Transformations import Transformations

#Centrage.transfo(test_csv2, 'dd')
