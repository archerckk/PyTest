#encoding=utf-8
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('程序运行')

def add(n):
    logging.debug('开始测试 add(%s)'%str(n))
    total=0
    for i in range(n):
        total+=i
        logging.debug('i is %s,total is %s'%(i,total))
    logging.debug('End of factorial(%s)'%str(n))
    return total
# print(add(10))
print(add(10))

logging.debug('程序运行完成')