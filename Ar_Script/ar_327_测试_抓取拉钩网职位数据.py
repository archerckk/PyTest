import requests
import csv
import time
import re
"""
1.请求带有查询关键字的职位信息网页的页面内容
2.要抓取职位信息，公司名称，URL，薪资待遇，公司规模，公司特点
3.打开URL抓取里到里面的职位描述（dd/job_bt），跟公司地址(job-address clearfix)
"""
str1='12K-15K'
def clear_data(str1):
    reg_num=re.compile(r'(\d{1,2})K-(\d{1,2})K',re.I)
    reg_result=re.match(reg_num,str1)
    lower=int(reg_result.group(1))*1000
    higher=int(reg_result.group(2))*1000
    # print(lower,higher)
    return lower,higher
assert clear_data(str1)==(12000,15000)

def get_data(page):
    base_url='https://www.lagou.com/jobs/positionAjax.json?gj=3-5%E5%B9%B4&px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'

    #表头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Accept':"application/json, text/javascript, */*; q=0.01",
        'Referer':'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88/p-city_213?px=default&gj=3-5%E5%B9%B4'
                }
    #参数信息
    form_data={
        'first':'true',
        'pn':page,
        'kd':'测试工程师'
    }

    s=requests.session()

    url_tmp='https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88/p-city_213?px=default&gj=3-5%E5%B9%B4'
    s.get(url_tmp,headers=headers)
    cookie=s.cookies

    res=s.post(base_url,data=form_data,headers=headers,cookies=cookie)

    result_json=res.json()
    position_list=result_json['content']['positionResult']['result']
    csv_file_info=[]

    for i in position_list:
        tmp_list=[]
        tmp_list.append(i['positionName'])
        tmp_list.append(i['companyShortName'])
        salary_result=clear_data(i['salary'])
        tmp_list.append(salary_result[0])
        tmp_list.append(salary_result[1])
        tmp_list.append(i['companySize'])
        tmp_list.append(i['financeStage'])
        tmp_list.append(i['companyLabelList'])
        tmp_list.append(i['education'])
        tmp_list.append(i['linestaion'])
        tmp_list.append(i['hitags'])
        csv_file_info.append(tmp_list)

    with open('position.csv','a+',newline='')as f:
        writer=csv.writer(f)
        writer.writerows(csv_file_info)

    return csv_file_info
if __name__ == '__main__':
    title=[('职位名称','公司简称','最低薪酬','最高薪酬','公司规模','财务状况','公司标签','学历要求','公司位置','公司优势')]
    with open('position.csv','w',newline='')as f:
        writer=csv.writer(f)
        writer.writerows(title)
    sum_page=[]
    for page_num in range(1,11):
        result=get_data(page_num)
        sum_page+=result
        print('已抓取{}页数据，总职位数为：{}个'.format(page_num,len(sum_page)))
        time.sleep(15)
















