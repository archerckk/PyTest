from xml.etree import ElementTree as et

'将没有用的xml里面的所有string标签的name属性都拿出来'

# target_file=et.parse('resources/香港多语言新加的.xml')
# target_root=et.XML(str_xml)
# target_root=target_file.getroot()
xml_file = et.parse('resources/gosms.xml')
root = xml_file.getroot()
attr_list = []
# count=0


'获取所有的string的name属性值放入列表'
for i in root:
    name_dict = i.attrib
    attr_list.append(name_dict['name'])

str_xml = open('resources/台湾多语言新加的.txt', 'r', encoding='GBK')

with open('resources/new_target2.txt', 'w', encoding='GBK')as f:
    for i in str_xml:
        a = i.partition('name="')
        b = a[2].partition('"')
        if b[0] not in attr_list:
            f.write(i)

# for i in target_file.findall('string'):
#     if i.attrib['name'] in attr_list:
#         target_root.remove(i)
#         # print(i.attrib['name'])#测试代码
# # for i in root2:
# #     print(i.attrib)
# target_file.write('resources/香港多语言新加的.xml')

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
