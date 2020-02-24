source=[5,3,4,2,1,1,2]
target=[1,2,3,4,5]

def select_sort(data:list):
    length=len(data)
    for i in range(length):
        min_num=i
        for j in range(i+1,length):
            if data[j]<data[min_num]:
                min_num=j
        data[i],data[min_num]=data[min_num],data[i]

    return data

def bubble_sort(data:list):
    length=len(data)
    for i in range(length):
        for j in range(length-i-1):#已经比较的数字就不再比较
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    return data


result=select_sort(source)
print(result)

result2=bubble_sort(source)
print(result2)