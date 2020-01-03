import sqlite3

connect=sqlite3.connect('beike.db')
c=connect.cursor()

sql='select * from price'
select_result=c.execute(sql)
price_dict={}

for row in select_result:
    if row[0] not in price_dict:
        price_dict[row[0]]=row[1]
    else:
        result=price_dict[row[0]]-row[1]
        if result <0:
            print("{}\t\t\t涨了{}\t\t\t现价为：{}".format(row[0],abs(result),row[1]).rjust(len(row[0])))
        elif result >0:
            print("{}\t\t\t跌了{}\t\t\t现价为：{}".format(row[0],abs(result),row[1]).rjust(len(row[0])))
        else:
            print('{}\t\t\t价格稳定\t\t\t现价为：{}'.format(row[0],row[1]).rjust(len(row[0])))
        price_dict[row[0]]=row[1]


