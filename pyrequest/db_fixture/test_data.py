import sys
sys.path.append('../db_fixture')
from mysql_db import DB
import time

def get_time():
    now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return now

#创建测试数据
datas={
'sign_event':[
    {'id':1,'name':'红米pro发布会','`limit`':2000,'status':1,'address':'北京会展中心',
     'start_time':get_time(),'create_time':get_time()},
    {'id':2,'name':'红米pro2发布会','`limit`':2000,'status':1,'address':'北京会展中心',
         'start_time':'2019-2-27 14:00:00','create_time':get_time()},
    {'id':3,'name':'红米pro3发布会','`limit`':2000,'status':1,'address':'北京会展中心',
         'start_time':'2019-3-20 14:00:00','create_time':get_time()},
    {'id':4,'name':'红米pro4发布会','`limit`':2000,'status':0,'address':'北京会展中心',
         'start_time':'2019-07-20 14:00:00','create_time':get_time()},
    {'id':5,'name':'红米pro5发布会','`limit`':2000,'status':0,'address':'北京会展中心',
         'start_time':'2019-12-20 14:00:00','create_time':get_time()},
    ],

'sign_guest':[
    {'id':1,'realname':'alen','phone':'12345678901','email':'alen@mail.com',
     'sign':0,'event_id':1,'create_time':get_time()},
    {'id':2,'realname':'jack','phone':'12345678902','email':'kack@mail.com',
         'sign':0,'event_id':1,'create_time':get_time()},
    {'id':3,'realname':'tom','phone':'12345678903','email':'tom@mail.com',
         'sign':0,'event_id':5,'create_time':get_time()},
    ]
}

def init_data():
    db=DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
        # db.close()

if __name__ == '__main__':
    init_data()