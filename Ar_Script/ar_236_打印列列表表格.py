tableData=[['apple','ban','cat','dog'],
           ['effects','function','game','hello'],
           ['ill','jack','king','lock']]
# table_dict={}
#
# for i in range(len(tableData)):
#     for j in range(len(tableData[i])):
#          if str(j) in table_dict.keys():
#             table_dict[str(j)]+=' '+tableData[i][j].center()
#          else:
#              table_dict[str(j)]=tableData[i][j]
#
# for v in table_dict.values():
#     print(v.center(10))


#参考答案
def findMaxWidth(target_list):
    maxWidth=0
    for i in range(len(target_list)):
        if len(target_list[i])>maxWidth:
            maxWidth=len(target_list[i])
    return maxWidth

print(findMaxWidth(tableData[1]))

def printTable(target):
    k=len(target)
    v=len(target[0])

    for i in range(v):
        for j in range(k):
            print(target[j][i].ljust(findMaxWidth(target[j])),end=' ')
        print()

printTable(tableData)