def get_digit(n):
    result = []
    while n>0:
        result.insert(0,n%10)
        n=n//10
    return result

print(get_digit(12345))