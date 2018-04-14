"""
有红、黄、蓝三种颜色的球，其中红球3个，黄球3个，绿球6个。
先将这12个球混合在一个盒子中，从中任意摸出8个球，编程计算摸出球的各种颜色搭配。
"""
print('red\t\tyellow\tbule')
for red in range(0,4):
    for yellow in range(0,4):
        for bule in range(0,7):
            if red+yellow+bule==8:
                # print(str(red)+'\t\t'+str(yellow)+'\t\t'+str(bule))
                #参考答案用法：
                print(red, '\t\t', yellow, '\t\t', bule)