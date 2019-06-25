def isSubSet(a,b):
    b=iter(b)

    return all(i in b for i in a)

print(isSubSet([1,3],[1,2,3]))


b=iter([1,2])
print(all(i in b for i in [1,2]))

a=(i for i in range(10))

for i in a:
    print(i)

print(next(a))