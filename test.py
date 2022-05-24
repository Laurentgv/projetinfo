from Importer.importer import Importer

doc1 = "/Users/laurentgv/Desktop/PTD - données/csv/synop.201301.csv.gz"
t1 = Importer.csv_file(doc1)
print (t1[0])

doc2 = "/Users/laurentgv/Desktop/PTD - données/json/2013-01.json.gz"
t2 = Importer.json_file(doc2)
print (t2[0])