from estimateur.correlation import Correlation
from estimateur.ecarttype import EcartType
from estimateur.moyenne import Moyenne
from estimateur.somme import Somme
from importer.importer import Importer
from table.table import Table
from table.transforme import Transforme
from estimateur.ecarttype import EcartType
from transformations.addweek import Addweek
from transformations.append import Append
from transformations.mapping import Mapping
#from transformations.normalisation import Normalisation
import time
from datetime import datetime
import outils
from transformations.transformation import Transformations
from transformations.typedate import Typedate
from transformations.meanbyvar import Meanbyvar
from transformations.makekey import Makekey
from figure.plot import Plot
from transformations.append import Append

def mega_json(L):
    data=[]
    for i in range(len(L)):
        data.append(Importer.json_file("/Users/Louis/Downloads/données/données_électricité/"+L[i]+".json.gz"))
    data_transf=[]
    for i in range(len(L)):
        data_transf.append(Transforme.transforme_json(data[i]))
    sortie=data_transf[0]
    for i in range(len(data_transf)):
        sortie=Append.transfo(sortie, data_transf[i])
    return sortie

def mega_csv(L):
    data=[]
    for i in range(len(L)):
        data.append(Importer.csv_file("/Users/Louis/Downloads/données/données_météo/synop."+L[i]+".csv.gz"))
    data_transf=[]
    for i in range(len(L)):
        data_transf.append(Transforme.transforme_csv(data[i], 'mq'))
    sortie=data_transf[0]
    for i in range(len(data_transf)):
        sortie=Append.transfo(sortie, data_transf[i])
    return sortie

def supp_var(entree, M):
    for i in M:
        Table.enlev_var(entree, i)
    return entree

###JSON
fichier_a_importer_json=["2013-01", "2013-02", "2013-03", "2013-04", "2013-05", "2013-06", "2013-07", "2013-08", "2013-09", "2013-10", "2013-11", "2013-12"]
variables_a_supp_json=['date', 'record_timestamp', 'heure', 'statut_terega', 'statut_rte', 'statut_grtgaz', 'fields', 'recordid', 'consommation_brute_gaz_terega', 'consommation_brute_electricite_rte', 'consommation_brute_gaz_grtgaz', 'consommation_brute_gaz_totale']
sortie_json=mega_json(fichier_a_importer_json)
sortie_json=Table.enlev_var(sortie_json, 'date')
sortie_json=Typedate.transfo(sortie_json, 'date_heure', '%Y-%m-%dT%H:%M:%S%z')
sortie_json=Addweek.transfo(sortie_json)
sortie_json=supp_var(sortie_json, variables_a_supp_json)
#conso=Table.extraire_var(sortie_json, 'consommation_brute_totale')
#week=Table.extraire_var(sortie_json, 'week')
#region=Table.extraire_var(sortie_json, 'region')
#conso_week=Table.add_var_special(week, conso.var[0],conso.data)
#cons_week_region=Table.ajouter_var(conso_week, region.var[0], region.data)
sortie_json=Makekey.transfo(sortie_json, 'region', 'week')
sortie_json=Table.enlev_var(sortie_json, 'region')
sortie_json=Table.enlev_var(sortie_json, 'week')
sortie_json=Meanbyvar.transfo(sortie_json, 'clé_regionweek')


###CSV
fichier_a_importer_csv=['201301', '201302', '201303', '201304', '201305', '201306', '201307', '201308', '201309', '201310', '201311', '201312']
sortie_csv=mega_csv(fichier_a_importer_csv)
sortie_csv=Typedate.transfo(sortie_csv, 'date', '%Y%m%d%H%M%S.0')
sortie_csv=Table.enlev_var(sortie_csv, '')

stations=Importer.csv_not_gz("/Users/Louis/Downloads/données/postesSynopAvecRegions.csv")
#il faut simplement transformer les id en num pour cohérence
for i in range(1, len(stations)):
    stations[i][0]=float(stations[i][0])
stations_table=Table(stations[0], stations[1:])
id=Table.extraire_var(stations_table, 'ID')
region=Table.extraire_var(stations_table, 'Region')
id_region=Table.add_var_special(id, region.var[0], region.data)

sortie_csv=Mapping.transfo(sortie_csv, 'numer_sta', id_region, 'ID', 'Region')
sortie_csv=Addweek.transfo(sortie_csv)
var_a_supp=['numer_sta', 'date', 'pmer', 'tend', 'cod_tend', 'dd', 'ff', 'td', 'u', 'vv', 'ww', 'w1', 'w2', 'n', 'nbas', 'hbas', 'cl', 'cm', 'ch', 'pres', 'niv_bar', 'geop', 'tend24', 'tn12', 'tn24', 'tx12', 'tx24', 'tminsol', 'sw', 'tw', 'raf10', 'rafper', 'per', 'etat_sol', 'ht_neige', 'ssfrai', 'perssfrai', 'rr1', 'rr3', 'rr6', 'rr12', 'rr24', 'phenspe1', 'phenspe2', 'phenspe3', 'phenspe4', 'nnuage1', 'ctype1', 'hnuage1','nnuage2', 'ctype2', 'hnuage2', 'nnuage3', 'ctype3', 'hnuage3', 'nnuage4', 'ctype4', 'hnuage4']
sortie_csv=supp_var(sortie_csv, var_a_supp)
sortie_csv=Makekey.transfo(sortie_csv, 'Region', 'week')
sortie_csv=Table.enlev_var(sortie_csv, 'Region')
sortie_csv=Table.enlev_var(sortie_csv, 'week')
sortie_csv=Meanbyvar.transfo(sortie_csv, 'clé_Regionweek')


###MERGE
Yes=Mapping.transfo(sortie_json, 'clé_regionweek', sortie_csv, 'clé_Regionweek', 't')
cor=Correlation(Table.extraire_var(Yes, 't').data).calcul(Table.extraire_var(Yes, 'consommation_brute_totale').data)
Plot(Table.extraire_var(Yes, 't')).scatlinreg(Table.extraire_var(Yes, 'consommation_brute_totale'), 'TEST')
