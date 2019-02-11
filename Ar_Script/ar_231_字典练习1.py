stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(target):
    print('Inventory:')
    sum=0
    for key,value in target.items():
        print('%s %s'%(value,key))
        sum+=value
    print('Total number of items:%d'%sum)

if __name__ == '__main__':
    displayInventory(stuff)