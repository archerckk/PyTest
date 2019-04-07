from pymysql import connect,cursors
from random import randint

host_list=['192.168.85.136','127.0.0.1','61.140.112.160']

conn=connect(host=host_list[2],
             port=3306,
             user='root',
             password='123456',
             db='test_data',
             charset='utf8mb4',
             cursorclass=cursors.DictCursor)

try:
    with conn.cursor()as cursor:
        for i in range (1,1000):
            id="%03d"%i
            sex=randint(0,1)
            age=randint(12,70)
            sql='INSERT INTO test_user(id,name,sex,age)VALUES (%d,"user_%s",%d,%d)'\
                %(i,id,sex,age)
            cursor.execute(sql)
    conn.commit()

    with conn.cursor()as cursor:
        sql='SELECT * from test_user WHERE name=%s'
        cursor.execute(sql,('user_001'))
        result = cursor.fetchone()
        print(result)

finally:
    conn.close()
