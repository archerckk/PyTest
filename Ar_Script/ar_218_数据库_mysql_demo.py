from pymysql import cursors,connect

#创建一个数据库链接
conn=connect(host='127.0.0.1',
             user='root',
             password='123456',
             db='guest',
             charset='utf8mb4',
             cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:#创建一个数据库操作游标对象（）
        #创建嘉宾数据
        sql='INSERT INTO sign_guest(realname,phone,email,sign,event_id,create_time)' \
            'VALUES("TOM",123456789,"TOM@mail.com",0,1,NOW());'

        cursor.execute(sql)#执行语句
    conn.commit()#提交数据库执行

    with conn.cursor()as cursor:
        sql="SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql,('123456789'))
        result=cursor.fetchone()
        print(result)
finally:
    conn.close()#关闭数据库连接