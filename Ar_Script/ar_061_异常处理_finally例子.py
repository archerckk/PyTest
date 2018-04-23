try:
    f = open('resources/存在.txt')
    print(f.read())
except IOError as reason:
    print('出错啦！'+str(reason))
    # f.close()
else:
    print('我只是打个酱油')
finally:
    print('我执行啦')


