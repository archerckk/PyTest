d = {'mike': 10, 'lucy': 2, 'ben': 30}

D=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
print(D)