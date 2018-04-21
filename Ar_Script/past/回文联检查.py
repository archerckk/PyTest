def huiwenlian():
    '''回文联是指顺着读跟倒着读文字显示的内容是一样的'''
    content=input('请输入一句话：')
    tmp=[]
    new=''
    for i in content:
        tmp.insert(0,i)
    for i in tmp:
        new+=i
    if  content==new:
        return '这是一个回文联'
    else:
         return  '这不是一个回文联'

print(huiwenlian())
