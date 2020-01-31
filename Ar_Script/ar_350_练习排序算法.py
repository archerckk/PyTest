source=[5,3,4,2,1]
target=[1,2,3,4,5]

def sort_select(data:list):
    length=len(data)
    for i in range(length):
        min_num=i
        for j in range(i+1,length):
            if data[j]<data[min_num]:
                min_num=j
        data[i],data[min_num]=data[min_num],data[i]

    return data

result=sort_select(source)
print(result)