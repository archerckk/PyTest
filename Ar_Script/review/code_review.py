from xml.etree import ElementTree as et



'多语言筛选脚本'
xml_file=et.parse('../resources/gosms.xml')
root=xml_file.getroot()
attrib_list=[]


for i in root:
    tmp_dict=i.attrib
    attrib_list.append(tmp_dict['name'])

str_file=open('../resources/台湾多语言新加的.txt','r',encoding='gbk')

with open('../resources/review_target.txt','w',encoding='gbk')as f:
    for i in str_file:
        a=i.partition('name="')
        b=a[2].partition('"')
        if b[0] not in attrib_list:
            f.write(i)


