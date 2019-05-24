name=input('请输入你的名字：')
gender=input('y/n：')

welcomeStr='Welcome {start} {name}'
nameDict={
    'start':'Mr.'if gender=='y'else 'Mrs',
     'name':name
}
print(welcomeStr.format(**nameDict))
