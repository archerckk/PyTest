list1=[]
def get_digit(n):
    if n>0:
        list1.insert(0, n%10)
        get_digit(n//10)

get_digit(12345)
print(list1)