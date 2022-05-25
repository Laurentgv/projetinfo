from estimateur.ecarttype import EcartType
from estimateur.moyenne import Moyenne
from estimateur.somme import Somme
from importer.importer import Importer
from table.Table import Table
from table.transforme import Transforme
from estimateur.ecarttype import EcartType

test_json=Importer.json_file("/Users/Louis/Downloads/données/données_électricité/2013-01.json.gz")
print(test_json[0])
test_json2=Transforme.transforme_json(test_json)

test_csv=Importer.csv_file("/Users/Louis/Downloads/données/données_météo/synop.201301.csv.gz")
test_csv2=Transforme.transforme_csv(test_csv, 'mq')
test_csv2.var
test_csv2.data

test_csv2.data[0]
print(test_csv2.data[0])
Somme(test_csv2.data[0]).calcul()
Moyenne(test_csv2.data[0]).calcul(None)
EcartType(test_csv2.data[0]).calcul()

from transformations.Centrage import Centrage
from transformations.Transformations import Transformations

Centrage.transfo(test_csv2, 'pmer')
