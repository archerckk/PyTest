#将广告列表跟品牌列表的里面的内容关联匹配起来，再打印出来
list1=['1.Just do It','2.一切皆有可能','3.让编程改变世界','4.Impossible is Nothing']
list2=['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3=[brand+":"+ad[2:]for ad in list1 for brand in list2 if ad[0]==brand[0]]

for i in list3:
    print(i)