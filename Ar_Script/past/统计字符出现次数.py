def count_str():
    list1=[]
    str1='dfdsfdsfdsfdsfdewrewrewgjyj676576576521321.0..0.0.dsfdsfs\ndsfdsfd3243242\ndsfdsfdsewrew324324....==-=-'
    for i in str1:
        if i not in list1:
            if i == '\n':
                print('\\n',str1.count('\n'))
            else:
                print(i,str1.count(i))
        list1.append(i)

count_str()