while 1:
    try:
        if i<5:
            print(i)
        else:
            break
        i+=1
    except NameError:
        i=0
