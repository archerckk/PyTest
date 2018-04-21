def bin2(n):
    result=""
    if n:
        result=bin(n//2)
        return result+str(n%2)
    else:
        return result


print(bin2(77))