import urllib.request as r
import chardet
import easygui as g



def main():
    '获取网络请求对象'
    msg = '请填写喵的尺寸'
    title = '下载一只猫'
    field = ['宽', '高']
    size = width, height = 600, 400
    fieldValues = []
    # response=r.urlopen('http://placekitten.com/g/%d/%d'%(100,200))
    '加入异常处理，假如无法识别尺寸的情况'
    while 1:

        if fieldValues == None:
            break
        errmsg = ""

        try:
            width = int(fieldValues[0].strip())
        except:
            errmsg += "宽度必须为整数！"

        try:
            height = int(fieldValues[1].strip())
        except:
            errmsg += "高度必须为整数！"

        if errmsg == "":
            break
        fieldValues = g.multenterbox(msg, title, field)
        '将请求对象的内容获取出来'
    response = r.urlopen('http://placekitten.com/g/%s/%s' % (fieldValues[0], fieldValues[1]))
    html=response.read()
    '识别网络地址编码形式'
    encode=chardet.detect(html)['encoding']
    if encode=='gb2312':
        encode='GBK'

    filepath = g.diropenbox("请选择存放喵的文件夹")

    '假如有选择路径择保存在目标目录，没有选择则保存在脚本所在目录'
    if filepath:
        filename = '%s/cat_%d_%d.jpg' % (filepath, width, height)
    else:
        filename = 'cat_%d_%d.jpg' % (width, height)

    # savaPath=g.filesavebox('请选择你要存放喵的地方','喵喵仓库','.jpg')
    with open(filename,'wb',encoding=encode)as f:
        '以二进制的方式打开一个JPG文件，写入请求对象的内容'
        f.write(html)

main()