import json

with open('resources/data1.json',encoding='utf-8')as f:
    data1_json=json.load(f)

with open('resources/data2.json',encoding='utf-8')as f:
    data2_json=json.load(f)




for day in data2_json['day_starts']:
    data1_json['day_starts'].append(day)


for item in data2_json['time_entries']:
    data1_json['time_entries'].append(item)

print(len(data1_json['day_starts']))
print(len(data1_json['time_entries']))


data1_json['base_work_times']=data2_json['base_work_times']
data1_json['meta']=data2_json['meta']
data1_json['preferences']=data2_json['preferences']
data1_json['settings']=data2_json['settings']
data1_json['time_entry_locations']=data2_json['time_entry_locations']
data1_json['time_owners']=data2_json['time_owners']



with open('data3.json','w')as f:
    json.dump(data1_json,f)