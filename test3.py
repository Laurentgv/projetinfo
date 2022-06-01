from matplotlib.pyplot import table
from estimateur.correlation import Correlation
from estimateur.ecarttype import EcartType
from estimateur.moyenne import Moyenne
from estimateur.somme import Somme
from importer.importer import Importer
from table.table import Table
from table.transforme import Transforme
from estimateur.ecarttype import EcartType
from transformations.addweek import Addweek
from transformations.mapping import Mapping
from transformations.normalisation import Normalisation
import time
from datetime import datetime
import outils
from transformations.transformation import Transformations
from transformations.typedate import Typedate
from transformations.meanbyvar import Meanbyvar
from transformations.makekey import Makekey



##JSON
test_json=Importer.json_file("/Users/Louis/Downloads/données/données_électricité/2013-01.json.gz")
test_json2=Transforme.transforme_json(test_json)
test_json3=Typedate.transfo(test_json2, 'date_heure', '%Y-%m-%dT%H:%M:%S+01:00')
test_json4=Table.enlev_var(test_json3, 'date')
test_json4=Table.enlev_var(test_json3, 'record_timestamp')
test_json4=Table.enlev_var(test_json3, 'heure')
test_json4=Table.enlev_var(test_json3, 'statut_terega')
test_json4=Table.enlev_var(test_json3, 'statut_rte')
test_json4=Table.enlev_var(test_json3, 'statut_grtgaz')
test_json4=Table.enlev_var(test_json3, 'fields')
test_json4=Table.enlev_var(test_json3, 'recordid')
test_json4=Table.enlev_var(test_json3, 'consommation_brute_gaz_terega')
test_json4=Table.enlev_var(test_json3, 'consommation_brute_electricite_rte')
test_json4=Table.enlev_var(test_json3, 'consommation_brute_gaz_grtgaz')
test_json4=Table.enlev_var(test_json3, 'consommation_brute_gaz_totale')
test_json5=Addweek.transfo(test_json4)
#Avant de moyenner par week il  faut extraire toutes les variables sur lesquels on veut faire des moyennes.
conso=Table.extraire_var(test_json5, 'consommation_brute_totale')
week=Table.extraire_var(test_json5, 'week')
region=Table.extraire_var(test_json5, 'region')
conso_week=Table.add_var_special(week, conso.var[0],conso.data)
cons_week_region=Table.ajouter_var(conso_week, region.var[0], region.data)

test_json6=Makekey.transfo(cons_week_region, 'region', 'week')
test_json7=Table.enlev_var(test_json6, 'region')
test_json7=Table.enlev_var(test_json6, 'week')
test_json8=Meanbyvar.transfo(test_json7, 'clé_regionweek')




##CSV
test_csv=Importer.csv_file("/Users/Louis/Downloads/données/données_météo/synop.201301.csv.gz")
test_csv2=Transforme.transforme_csv(test_csv, 'mq')
test_csv3=Typedate.transfo(test_csv2, 'date', '%Y%m%d%H%M%S.0')

stations=Importer.csv_not_gz("/Users/Louis/Downloads/données/postesSynopAvecRegions.csv")
#il faut simplement transformer les id en num pour cohérence
for i in range(1, len(stations)):
    stations[i][0]=float(stations[i][0])

stations_table=Table(stations[0], stations[1:])

#Comme on a besoin de l'unicité de la clé il faut donner les semaines avant
#test_csv4=Mapping.transfo(test_csv3, 'numer_sta', stations, 'ID', 'Region')
test_csv4=Table.enlev_var(test_csv3, '')
id=Table.extraire_var(stations_table, 'ID')
region=Table.extraire_var(stations_table, 'Region')
id_region=Table.add_var_special(id, region.var[0], region.data)
test_csv5=Mapping.transfo(test_csv3, 'numer_sta', id_region, 'ID', 'Region')
test_csv6=Addweek.transfo(test_csv5)
test_csv7=Table.enlev_var(test_csv6, 'numer_sta')
test_csv7=Table.enlev_var(test_csv6, 'date')
test_csv7=Table.enlev_var(test_csv6, 'pmer')
test_csv7=Table.enlev_var(test_csv6, 'tend')
test_csv7=Table.enlev_var(test_csv6, 'cod_tend')
test_csv7=Table.enlev_var(test_csv6, 'dd')
test_csv7=Table.enlev_var(test_csv6, 'ff')
test_csv7=Table.enlev_var(test_csv6, 'td')
test_csv7=Table.enlev_var(test_csv6, 'u')
test_csv7=Table.enlev_var(test_csv6, 'vv')
test_csv7=Table.enlev_var(test_csv6, 'ww')
test_csv7=Table.enlev_var(test_csv6, 'w1')
test_csv7=Table.enlev_var(test_csv6, 'w2')
test_csv7=Table.enlev_var(test_csv6, 'n')
test_csv7=Table.enlev_var(test_csv6, 'nbas')
test_csv7=Table.enlev_var(test_csv6, 'hbas')
test_csv7=Table.enlev_var(test_csv6, 'cl')
test_csv7=Table.enlev_var(test_csv6, 'cm')
test_csv7=Table.enlev_var(test_csv6, 'ch')
test_csv7=Table.enlev_var(test_csv6, 'pres')
test_csv7=Table.enlev_var(test_csv6, 'niv_bar')
test_csv7=Table.enlev_var(test_csv6, 'geop')
test_csv7=Table.enlev_var(test_csv6, 'tend24')
test_csv7=Table.enlev_var(test_csv6, 'tn12')
test_csv7=Table.enlev_var(test_csv6, 'tn24')
test_csv7=Table.enlev_var(test_csv6, 'tx12')
test_csv7=Table.enlev_var(test_csv6, 'tx24')
test_csv7=Table.enlev_var(test_csv6, 'tminsol')
test_csv7=Table.enlev_var(test_csv6, 'sw')
test_csv7=Table.enlev_var(test_csv6, 'tw')
test_csv7=Table.enlev_var(test_csv6, 'raf10')
test_csv7=Table.enlev_var(test_csv6, 'rafper')
test_csv7=Table.enlev_var(test_csv6, 'per')
test_csv7=Table.enlev_var(test_csv6, 'etat_sol')
test_csv7=Table.enlev_var(test_csv6, 'ht_neige')
test_csv7=Table.enlev_var(test_csv6, 'ssfrai')
test_csv7=Table.enlev_var(test_csv6, 'perssfrai')
test_csv7=Table.enlev_var(test_csv6, 'rr1')
test_csv7=Table.enlev_var(test_csv6, 'rr3')
test_csv7=Table.enlev_var(test_csv6, 'rr6')
test_csv7=Table.enlev_var(test_csv6, 'rr12')
test_csv7=Table.enlev_var(test_csv6, 'rr24')
test_csv7=Table.enlev_var(test_csv6, 'phenspe1')
test_csv7=Table.enlev_var(test_csv6, 'phenspe2')
test_csv7=Table.enlev_var(test_csv6, 'phenspe3')
test_csv7=Table.enlev_var(test_csv6, 'phenspe4')
test_csv7=Table.enlev_var(test_csv6, 'nnuage1')
test_csv7=Table.enlev_var(test_csv6, 'ctype1')
test_csv7=Table.enlev_var(test_csv6, 'hnuage1')
test_csv7=Table.enlev_var(test_csv6, 'nnuage2')
test_csv7=Table.enlev_var(test_csv6, 'ctype2')
test_csv7=Table.enlev_var(test_csv6, 'hnuage2')
test_csv7=Table.enlev_var(test_csv6, 'nnuage3')
test_csv7=Table.enlev_var(test_csv6, 'ctype3')
test_csv7=Table.enlev_var(test_csv6, 'hnuage3')
test_csv7=Table.enlev_var(test_csv6, 'nnuage4')
test_csv7=Table.enlev_var(test_csv6, 'ctype4')
test_csv7=Table.enlev_var(test_csv6, 'hnuage4')

#il faut créer la clé unique
test_csv8=Makekey.transfo(test_csv7, 'Region', 'week')
test_csv9=Table.enlev_var(test_csv8, 'Region')
test_csv9=Table.enlev_var(test_csv8, 'week')
test_csv9=Table(test_csv9.var, test_csv9.data[:-1])

test_csv10=Meanbyvar.transfo(test_csv9, 'clé_Regionweek')


#13:53 seems like everything works
#manque plus que le join entre temp et conso sur les variables clé

Yes=Mapping.transfo(test_json8, 'clé_regionweek', test_csv10, 'clé_Regionweek', 't')

cor=Correlation(Table.extraire_var(Yes, 't').data).calcul(Table.extraire_var(Yes, 'consommation_brute_totale').data)

EcartType(Table.extraire_var(Yes, 'consommation_brute_totale').data).calcul()
EcartType(Table.extraire_var(Yes, 't').data).calcul()
