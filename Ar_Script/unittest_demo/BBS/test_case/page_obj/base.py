class Page(object):
    '''
    页面基类，用于所有页面的继承
    
    初始化，地址，驱动，超时时间
    打开网页方法
    查找单个元素方法
    查找多个元素方法
    页面打开检查
    调用JavaScript代码
    '''
    bbs_url='https://mail.qq.com'

    def __init__(self,selenium_driver,base_url=bbs_url,parent=None):
        self.base_url=base_url
        self.timeout=30
        self.driver=selenium_driver
        self.parent=parent

    def _open(self,url):
        self.url=self.base_url+url
        self.driver.get(self.url)
        assert self.on_page() ,'【%s】打开失败'%self.url

    def open(self):
        return self._open(self.url)

    def on_page(self):
        print(self.driver.current_url)
        return self.driver.current_url==(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elments(self,*loc):
        return self.find_elments(*loc)

    def script(self,src):
        return self.driver.execute_script(src)