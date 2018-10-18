from xml.etree import ElementTree as et

'将没有用的xml里面的所有string标签的name属性都拿出来'


xml_file=et.parse('resources/gosms.xml')
root=xml_file.getroot()
count=0
attr_list=[]

'获取所有的string的name属性值放入列表'
for i in root:
    name_dict=i.attrib
    attr_list.append(name_dict['name'])


for i in root.findall('string'):
    if i.attrib['name'] in attr_list:
        # root.remove(i)
        print(i.attrib['name'])#测试代码
# for i in root2:
#     print(i.attrib)
# xml_file.write('resources/gosms.xml')

'打印所有属性值'
# for i in attr_list:
#     count+=1
#     print(i)
# print(count)
# str1=root.getElementsByTagName('string')
# for i in str1:
#     print(i.tag)
#
# print(str1[0].getAttribute)