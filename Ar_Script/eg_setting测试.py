import easygui as g



try:
        print('I Love FishC.com!')
        int('FISHC') # 这里会产生异常
except:
        g.exceptionbox()