list1=['1.Just do it.','2.一切皆有可能','3.让变成改变世界','4.Nothing is impossible']
list2=['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3=[brand+':'+ad[2:] for ad in list1 for brand in list2 if brand[0]==ad[0]]

for i in list3:
    print(i)

