import json



def get_fomat():
    result_dict={}
    with open('./header_fomat.txt','r')as f:
        content=f.readlines()
        for line in content:
            key,value=line.split(':')
            result_dict[key]=value.strip()

    with open('./header_fomat.txt','w')as f:
           json.dump(result_dict,f,indent=1)

def post_fomat():
    str_dict={}
    str1=input('请输入你要格式化的body参数：')
    tmp_str=str1.split('&')
    for i in tmp_str:
        key,value=i.split('=')
        str_dict[key]=value
    str_dict=json.dumps(str_dict,indent=1)
    print(str_dict)


while 1:
    choice=input('请选择你要格式化的方法(1:get,2:post,3:退出)：')

    if choice=='1':
        get_fomat()
        print('header_fomat.txt内容已经变更！')
    elif choice=='2':
        post_fomat()
    else:
        print('退出程序!')
        break

