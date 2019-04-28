import shutil,os,re

'修改工作目录到result目录下方'
os.chdir(os.curdir+os.sep+'result')
file_list=os.listdir(os.getcwd())

'匹配html文件'
file_reg=re.compile(r'(\d+)_(\d+)_(\d+)_(\d+)_(\d+)_(\d+)(.+)\.html')
for i in file_list:
    reg_result=file_reg.search(i)
    if reg_result!=None:
        new_name=reg_result.group().replace(reg_result.group(7),'&'+reg_result.group(7))
        print(new_name)
        shutil.move(i,new_name)
