while 1:
    try:
        if i<5:
            print(i)
        else:
            break
        i+=1
    except NameError:
        i=0

'参考答案：'
alist = range(5)
it = iter(alist)

while True:
    try:
        print(next(it))
    except StopIteration:
        break