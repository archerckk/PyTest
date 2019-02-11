import ar_231_字典练习1 as show

stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
add_list=['rope','rope','gold coin','arrow','torch','dagger','kong']

def addInventory(target,add_list):
    for i in add_list:
        if  i in stuff.keys():
            stuff[i]+=1
        else:
            stuff[i]=1

addInventory(stuff,add_list)

show.displayInventory(stuff)