from zope.interface import Interface
from zope.interface.declarations import implementer

#定义接口
class IHost(Interface):
    def goodmorning(self,host):
        '''Say good morning to host'''

#继承接口（实现接口）
@implementer(IHost)
class Host:
    def goodmoring(self,guest):
        '''Say good morning to guest'''
        return '''Good morning,%s!'''%(guest)

#测试接口的具体实现
host=Host()
print(host.goodmoring('Tom'))