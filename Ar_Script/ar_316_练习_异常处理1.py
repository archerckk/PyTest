import requests
import os

#1 定义一个函数func(filename) filename:文件的路径，函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。
def func(filename):
    try:
        file=open(filename)
        content=file.read()

    except OSError as e:
        print ('文件打开失败：{}'.format(e))
    finally:
        # nonlocal file
        file.close()
    return content
# file_path='./mailList.txt'
# content=func(file_path)
# print(content)
# print(func("123"))

#2 定义一个函数func(urllist)   urllist:为URL的列表，例如：['http://xx.com','http://www.xx.com','http://www.xxx.com'...]

#函数功能：要求依次打开url，打印url对应的内容，如果有的url打不开，则把url记录到日志文件里，并且跳过继续访问下个url。

def func2(urlliist):
    for i in urlliist:
        try:
            body=requests.get(i)
            print(body.text)
        except requests.exceptions.ConnectionError as e:
            errFile=open('errFile.txt','a')
            errFile.write("error_url:{},message:{}\n".format(i, str(e)))
            errFile.close()
            continue
        except requests.exceptions.MissingSchema as e:
            errFile = open('errFile.txt', 'a')
            errFile.write("error_url:{},message:{}\n".format(i, str(e)))
            errFile.close()
            continue
        except TimeoutError as e:
            errFile = open('errFile.txt', 'a')
            errFile.write("error_url:{},message:{}\n".format(i,str(e)))
            errFile.close()
            continue

# urllist=['http://www.vgooo.com/','123','http://www.xxx.com']
# func2(urllist)

#3 定义一个函数func(domainlist)   domainlist:为域名列表，例如：['xx.com','www.xx.com','www.xxx.com'...]
#函数功能：要求依次ping 域名，如果ping 域名返回结果为：request time out，则把域名记录到日志文件里，并且跳过继续ping下个域名。（提示用os模块的相关方法）
def func3(domainlist):
    file=open('domainLog.txt','a')
    for item in domainlist:
        content=os.popen('ping {}'.format(item)).read()

        if "请求超时"in content:
            file.write(content+"\n")
    file.close()

# domainList=['xx.com','www.xx.com','www.xxx.com']
# func3(domainList)


#4 定义一个函数func(filename) filename:为文件名，用with实现打开文件，并且输出文件内容。
def func4(filename):

  try:
    with open(filename)as f:
        print(f.read())
  except IOError:
      return "文件传入有误，无法正常打开"

assert func4('123')=="文件传入有误，无法正常打开"
func4('domainLog.txt')



#5 定好一个函数func(listinfo) listinfo:为列表，listinfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555] 返回一个列表包含小于100的偶数，并且用assert来断言
#返回结果和类型。

def func5(listInfo):
    result=[]
    for i in listInfo:
        if (i%2==0) and (i<100):
            result.append(i)

    return result

listInfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555]
assert func5(listInfo)==[88, 22, 44, 44, 22, 66]
assert type(func5(listInfo))==list

#6 自己定义一个异常类，继承Exception类, 捕获下面的过程：判断raw_input()输入的字符串长度是否小于5，如果小于5，比如输入长度为3则输出:" The input is of length 3,expecting at least 5'，大于5输出"print success'

class MyException(Exception):

    def __init__(self,length):
        self.length=length
        if self.length<5:
            print(" The input is of length {},expecting at least 5".format(self.length))
        else:
            print('print success')


try:
    length = len(input("请输入字符串："))
    raise MyException(length)
except MyException as e:
    print(e)
