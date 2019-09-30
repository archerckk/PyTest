#encoding=utf-8
import requests
import os

#1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
def get_num(num):
    result=[]
    if isinstance(num,list):
        for i in num:
            if isinstance(i, int):
                result.append(i)
            else:
                return '列表包含非数字元素，返回默认列表{}'.format([2,4,6])
        return result
    else:
        return "传入的参数不是列表,返回默认列表{}".format([2,4,6])


assert get_num("123")== "传入的参数不是列表,返回默认列表{}".format([2,4,6])
assert get_num([1,'a',3])=='列表包含非数字元素，返回默认列表{}'.format([2,4,6])
assert get_num([1,23,4])==[1,23,4]



#2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。

str1="""<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>æ°é»</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å°å¾</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>è§é¢</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å§</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>ç»å½</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">ç»å½</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ´å¤äº§å</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>å³äºç¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç¨ç¾åº¦åå¿è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æè§åé¦</a>&nbsp;äº¬ICPè¯030173å·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>
"""
def get_page(url):
    try:
        body=requests.get(url)
        if body.status_code == 200:
            content = body.text
            return content
    except Exception as error:

        return '你输入的网址有误，无法获取到网页信息'
assert get_page('http://www.baidu.com1')=='你输入的网址有误，无法获取到网页信息'
print(get_page("http://www.baidu.com"))


#3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
def func(*listItems):
    """
    1、遍历所有的列表元素
    2、遍历所有的列表元素里面的所有元素放进去一个列表里面
    3、排序这个列表，返回最大的那个元素
    """
    tmp_list=[]

    for item in listItems:
        if isinstance(item,list):
            for i in item:
                tmp_list.append(i)

    tmp_list=list(filter(lambda k:isinstance(k,int),tmp_list))
    tmp_list.sort(reverse=True)
    max_value=tmp_list[0]

    return max_value

assert func([1,2,3,'a'])==3
assert func([1,2,3,'a'],'aaaa',True,[7,8,9,999])==999


#4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
def get_dir(f):
    """
    1、判断f是否为一个有效的路径
        是，则执行第二步
        否，则返回一个无效文件的错误信息
    2、获取f路径下面的所有文件，判断文件的类型
        包含文件，则输出文件夹路径列表
        不包含文件，则输出Not dir
    """
    if os.path.exists(f):
        fileList=os.listdir(f)
        # print(fileList)
        result=[]
        for file in fileList:
            if os.path.isdir(f+os.sep+file):
                result.append(f+os.sep+file)
        if result==[]:
            return 'Not dir'
        return result
    else:
        return '文件路径不存在'
resultList=['D:\\Download\\0902基础包', 'D:\\Download\\apk', 'D:\\Download\\apk(1)', 'D:\\Download\\apk(1)(1)', 'D:\\Download\\apk(2)', 'D:\\Download\\apk(3)', 'D:\\Download\\apk(4)', 'D:\\Download\\apk2', 'D:\\Download\\aptz', 'D:\\Download\\BtResourceSearch', 'D:\\Download\\Bunny Puzzle', 'D:\\Download\\BunnyPuzzle', 'D:\\Download\\debug', 'D:\\Download\\Filter Art', 'D:\\Download\\HamsterPuzzle', 'D:\\Download\\json压缩工具', 'D:\\Download\\Love Test Yo', 'D:\\Download\\LoveTester', 'D:\\Download\\Meow Puzzle', 'D:\\Download\\newSleep', 'D:\\Download\\PaintCamera', 'D:\\Download\\PaintCamera(1)', 'D:\\Download\\pics_Hamster Puzzle', 'D:\\Download\\pics_Meow Puzzle', 'D:\\Download\\pics_pintu0715', 'D:\\Download\\pics_Pokemon Puzzle', 'D:\\Download\\pics_Puppy Puzzle', 'D:\\Download\\pics_Shiba Inu Puzzle', 'D:\\Download\\PuppyPuzzle', 'D:\\Download\\Puzzle Puppies2', 'D:\\Download\\PuzzleKittens', 'D:\\Download\\Shiba Inu Puzzle', 'D:\\Download\\SleepClock', 'D:\\Download\\travel', 'D:\\Download\\utorrentportable_3.5.5.45311', 'D:\\Download\\WIN10 xl5_31698', 'D:\\Download\\Xshell+6', 'D:\\Download\\xunkeifhb5xz', 'D:\\Download\\xunkeifhb5xz (2)', 'D:\\Download\\__MACOSX', 'D:\\Download\\广告缓存', 'D:\\Download\\查重', 'D:\\Download\\正式包']

assert get_dir(r'D:\Download')==resultList
assert get_dir(r'D:\Download1')=='文件路径不存在'
assert get_dir(r'D:\script')=='Not dir'

#注明：吸取上次作业遇到的问题，要求写的函数逻辑清楚，并且考虑一些特殊的情况处理，能做断言的尽量用断言。