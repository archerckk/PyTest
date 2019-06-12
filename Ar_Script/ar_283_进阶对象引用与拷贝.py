import copy

x=[1]
x.append(x)
z=[1,[1,[1,[1]]]]
print(len(x))
print(len(z))
y=copy.deepcopy(x)



print(x==y)