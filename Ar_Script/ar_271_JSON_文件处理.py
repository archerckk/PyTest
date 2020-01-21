import json

parms={
    'name':'Tom',
    'gender':'Man',
    'age':17
}

with open('result/271.json','w')as file:
    json.dump(parms,file)

with open('result/271.json')as file:
    jsonContent=json.load(file)

for i in jsonContent.items():
    print(i[0], i[1])