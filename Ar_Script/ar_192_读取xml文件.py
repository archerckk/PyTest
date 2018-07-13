from xml.dom import minidom

dom=minidom.parse('resources/test.xml')

root=dom.documentElement

'获取tag名称'
tagname=root.getElementsByTagName('test')
'注意tagName是要大写的'
print(tagname[0].tagName)

'获取tag的属性'
logins=root.getElementsByTagName('login')
username=logins[0].getAttribute('username')
print(username)

'获取标签下面的值'
provices=root.getElementsByTagName('provice')
data=provices[1].firstChild.data
print(data)
