#encoding=utf-8

import requests

"""
题目一： 写一个网页数据操作类。完成下面的功能：

提示：需要用到urllib模块

get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int 

get_htmlcontent() 获取网页的内容。返回类型:str

get_linknum()计算网页的链接数目。
"""

class Url_info:

    def __init__(self,url):
        self.url=url
        self.body=requests.get(url)


    def get_httpcode(self):
        return self.body.status_code

    def get_htmlcontent(self):
        return self.body.text

    def get_linknum(self):

        return self.body.text.count('a href=')

url_info=Url_info('http://www.vgooo.com/')
print(url_info.get_htmlcontent())
print(url_info.get_httpcode())
print(url_info.get_linknum())

"""
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        '''Tell my details.'''
        print 'Name:"%s" Age:"%s"' % (self.name, self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
        print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tell(self):
        print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]
for member in members:
    member.tell()
    
体会下这段代码，把结果的执行流程用自己的话写下。
"""

"""
1、先新建一个学校人的基类，初始化姓名跟年龄两个变量，打印姓名，编写一个说方法，打印姓名和年龄
2、新建一个教师类，继承学校人基类，初始化姓名跟工资两个变量，打印教师名字，重写说方法，打印姓名和工资
3、新建一个学生类，继承学校人基类，初始化姓名跟成绩两个变量，打印学生名字，重新说方法，打印姓名和成绩
4、实例化教师类跟学生类，将两个实例对象放进去一个列表，遍历列表执行实例对象的tell方法
"""