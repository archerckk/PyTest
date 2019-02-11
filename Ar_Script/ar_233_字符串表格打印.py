
def print_dict_table(target,leftWidth,rightWidth):
    print('Items List'.center(leftWidth+rightWidth,'-'))

    for k,v in target.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(1))


stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
print_dict_table(stuff,15,10)
