test=[123,456,2,78,9]
def max(test):
    max=test[0]
    for i in test:
        if i>max:
            max=i
    return max
target=max(test)
print('%d当中的最大值为'%target)