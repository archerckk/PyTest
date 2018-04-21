import easygui as g

result=g.multchoicebox(msg='挑一些奇奇怪怪的东西',title='选择列表',choices=['以为你只是一个美丽的偶然','垂怜我不经意降落',
                                                   '谁知道你同','谁知道你不走','拥抱着我说终于找到了我'])
print(result)