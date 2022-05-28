import outils
from table.Table import Table


#L=Table(['yo','yo1','yo2'],[[1,2,3],[1,3,4]])
#L2=L.enlev_var('yo1')
#print(L2.data)


a=Table(["pays","temperature"],[["France",12],["UK",14]])
L2=a.enlev_var("temperature")
print(L2.var)

#Table([pays],[[France],[UK]])