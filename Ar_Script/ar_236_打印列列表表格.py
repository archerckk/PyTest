tableData=[['apple','ban','cat','dog'],
           ['effects','function','game','hello'],
           ['ill','jack','king','lock']]
table_dict={}

for i in range(len(tableData)):
    for j in range(len(tableData[i])):
         if str(j) in table_dict.keys():
            table_dict[str(j)]+=' '+tableData[i][j].center()
         else:
             table_dict[str(j)]=tableData[i][j]

for v in table_dict.values():
    print(v.center(10))
