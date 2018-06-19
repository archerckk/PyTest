import re
import json


def start(level):
    return '  '*level+'+'

def end(level):
    return '  '*level+'-'


def find_dict(targets,level):
    keys=iter(targets)
    for i in keys:
        if type(targets[i]) is not dict:
            print(end(level)+i)
        else:
            next_level=level+1
            print(start(level)+i)
            find_dict(targets[i],next_level)


def main():
    with open('resources/taobao.txt','r',encoding='utf-8')as f:
        g_page_config=re.search(r'g_page_config = (.*?);\n',f.read())
        # with open('resources/taobao2.txt', 'w', encoding='utf-8')as f:
        #     f.write(g_page_config.group(1))
        page_config=json.loads(g_page_config.group(1))
        find_dict(page_config,1)

if __name__ == '__main__':
    main()


