import sqlite3
import csv

def print_price(result):

    if result < 0:
        print("{}\t\t\t涨了{}\t\t\t现价为：{}\t\t\t{}".format(row[0], abs(result), row[1],row[3]))
        result_list.append([row[0], '涨了{}'.format(abs(result)), row[1],row[3]])
    elif result > 0:
        print("{}\t\t\t跌了{}\t\t\t现价为：{}\t\t\t{}".format(row[0], abs(result), row[1],row[3]))
        result_list.append([row[0], '跌了{}'.format(abs(result)), row[1], row[3]])
    else:
        print('{}\t\t\t价格稳定\t\t\t现价为：{}\t\t\t{}'.format(row[0], row[1],row[3]))
        result_list.append([row[0], '价格稳定', row[1], row[3]])

def data_save(result_list):
    f = open('beike.csv', 'w', newline='')
    title = ['楼盘名字', '价格走势', '现价', '时间']
    writer = csv.writer(f)
    writer.writerow(title)
    writer.writerows(result_list)
    f.close()

connect=sqlite3.connect('beike.db')
c=connect.cursor()

sql='select * from price'
select_result=c.execute(sql)
price_dict={}
result_list = []

for row in select_result:
    if row[0] not in price_dict:
        price_dict[row[0]]=row[1]
    else:
        result=price_dict[row[0]]-row[1]
        print_price(result)
        price_dict[row[0]]=row[1]

# data_save(result_list)

