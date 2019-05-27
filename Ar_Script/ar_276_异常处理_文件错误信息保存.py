import traceback
import logging as log
try:
    raise SyntaxError
except:
    with open('tracebackError.txt','w')as f:
        f.write(traceback.format_exc())
    print('错误信息保存到了tracebackError.txt当中')

log.basicConfig(level=log.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
log.disable(log.DEBUG)

log.debug('打印测试日志')
# log.disable(log.DEBUG)