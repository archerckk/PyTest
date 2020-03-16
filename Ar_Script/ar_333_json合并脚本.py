import json

with open('resources/data1.json',encoding='utf-8')as f:
    data1_json=json.load(f)

with open('resources/data2.json',encoding='utf-8')as f:
    data2_json=json.load(f)




for day in data1_json['day_starts']:
    data2_json['day_starts'].append(day)


for item in data1_json['time_entries']:
    data2_json['time_entries'].append(item)

print(len(data2_json['day_starts']))
print(len(data2_json['time_entries']))

with open('data3.json','w')as f:
    json.dump(data2_json,f)