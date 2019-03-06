from pymysql import connect,cursors
from random import randint


conn=connect(host='127.0.0.1',
             user='root',
             password='123456',
             db='test_data',
             charset='utf8mb4',
             cursorclass=cursors.DictCursor)
id=1

try:
    with conn.cursor()as cursor:
        for i in range (1,1000):
            id="%03d"%i
            sex=randint(0,1)
            age=randint(12,70)
            sql='INSERT INTO test_user(id,name,sex,age)VALUES (i,user_%s,%d,%d)'%(id,sex,age)
finally:
    conn.close()
