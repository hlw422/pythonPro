# -*- coding: utf-8 -*-
# 批量生成测试数据,并保存到mysql
from faker import Faker
from datetime import datetime
import random
import pymysql

def get_random_num20():
    """
    返回20位有效数字
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    random_num = "%06d" % random.randint(0, 1000000)
    return '%s%s' % (str(now), str(random_num))

def create_test_datas():
    # 创建一个faker对象
    fake = Faker('zh_CN')
    try:
        # 创建一个数据库连接
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='wxdata', charset='utf8')
        print('连接mysql成功')
        # 创建一个游标
        cursor = conn.cursor()
        # 创建一个sql语句
        sql = "INSERT INTO platpay_main (COMM_SN, PAY_TYPE, COMM_MAIN, TRADE_NO, \
BIZ_TYPE, TXN_TYPE, HOS_ID, USER_ID, USER_NAME, BUYER_ID, BUYER_NAME,\
 SFZ_NO, HIS_BUYER_ID, JE_ALL, JE_YB, CASH_JE, COMM_HIS, CREATE_TIME, \
BODY, TOKEN, REAL_CLIENT_ID, CLIENT_ID, BIZ_SN, HIS_SN, NOTIFY_TIME, \
HIS_CONFIRM_PERIOD, HIS_CONFIRM_NAME, HIS_CONFIRM_RESULT, NOTIFY_URL, CHANNEL, \
CHANNEL_TYPE, YQBZ, DIRECT_PARAMS, AUTO_REFUND, LINK_COMM_SN, LINK_PAY_TYPE, \
EXPIRE_MINUTES, TRANS_MODE, TRANS_TXN_TYPE, BY1, BY2, BY3)\
        VALUES (%s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s,\
                 %s,%s, %s, %s, %s, %s,\
                 %s, %s, %s, %s, %s, %s,\
               %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s,\
                     %s, %s, %s, %s, %s, %s\
                   );"  # 创建一个sql语句
        # 循环生成数据
        for i in range(1, 1000):
            for j in range(1000):
                # 生成数据
                comm_sn = str(get_random_num20())
                pay_type = str(fake.random_int(min=1, max=2))
                comm_main = str(get_random_num20())
                TRADE_NO = str(get_random_num20())
                BIZ_TYPE = fake.random_int(min=1, max=6)
                TXN_TYPE =  "01" if fake.random_int(min=1, max=2)%2==0 else "02"
                HOS_ID=str(fake.random_int(min=1, max=1000))
                USER_ID=str(fake.random_int(min=1, max=1000))            
                USER_NAME=fake.name()
                BUYER_ID=fake.random_int(min=1, max=1000)
                BUYER_NAME=fake.name()
                SFZ_NO=fake.ssn()
                HIS_BUYER_ID=fake.random_int(min=1, max=1000)
                JE_ALL=fake.random_int(min=1, max=1000000)
                JE_YB=fake.random_int(min=1, max=1000000)
                CASH_JE=fake.random_int(min=1, max=1000000)            
                COMM_HIS=fake.random_int(min=1, max=1000000)
                CREATE_TIME=fake.date_time_this_year()
                BODY=fake.text(20)
                TOKEN=fake.uuid4()
                REAL_CLIENT_ID=fake.random_int(min=1, max=1000)
                CLIENT_ID=fake.random_int(min=1, max=1000)
                BIZ_SN=fake.random_int(min=1, max=1000)
                HIS_SN=fake.random_int(min=1, max=1000)             
                NOTIFY_TIME=fake.date_time_this_year()
                HIS_CONFIRM_PERIOD=fake.random_int(min=1, max=1000)
                HIS_CONFIRM_NAME=fake.name()
                HIS_CONFIRM_RESULT=fake.random_int(min=1, max=2)
                NOTIFY_URL=fake.url()         
                CHANNEL=fake.random_int(min=1, max=1000),
                CHANNEL_TYPE=fake.random_int(min=1, max=2)
                YQBZ=fake.random_int(min=1, max=2)                   
                DIRECT_PARAMS=fake.text(20)
                AUTO_REFUND=fake.random_int(min=1, max=2)
                LINK_COMM_SN=fake.random_int(min=1, max=1000)
                LINK_PAY_TYPE=fake.random_int(min=1, max=2)               
                EXPIRE_MINUTES=fake.random_int(min=1, max=100)
                TRANS_MODE=fake.random_int(min=1, max=2)
                TRANS_TXN_TYPE=fake.random_int(min=1, max=2)
                BY1=fake.random_int(min=1, max=10)
                BY2=fake.random_int(min=1, max=10)
                BY3=fake.random_int(min=1, max=100)
                
                
                # 执行sql语句
               
                
                print(cursor.mogrify(sql,  (comm_sn,pay_type,comm_main,TRADE_NO,BIZ_TYPE,TXN_TYPE,
                                    HOS_ID,USER_ID,USER_NAME,BUYER_ID,BUYER_NAME,SFZ_NO,HIS_BUYER_ID,
                                    JE_ALL,JE_YB,CASH_JE,COMM_HIS,CREATE_TIME,BODY,TOKEN,REAL_CLIENT_ID,CLIENT_ID,BIZ_SN,HIS_SN,
                                    NOTIFY_TIME,HIS_CONFIRM_PERIOD,HIS_CONFIRM_NAME,HIS_CONFIRM_RESULT,NOTIFY_URL,
                                    CHANNEL,CHANNEL_TYPE,YQBZ,DIRECT_PARAMS,AUTO_REFUND,LINK_COMM_SN,LINK_PAY_TYPE,
                                    EXPIRE_MINUTES,TRANS_MODE,TRANS_TXN_TYPE,BY1,BY2,BY3)))
                
                
                cursor.execute(sql, (comm_sn,pay_type,comm_main,TRADE_NO,BIZ_TYPE,TXN_TYPE,
                                    HOS_ID,USER_ID,USER_NAME,BUYER_ID,BUYER_NAME,SFZ_NO,HIS_BUYER_ID,
                                    JE_ALL,JE_YB,CASH_JE,COMM_HIS,CREATE_TIME,BODY,TOKEN,REAL_CLIENT_ID,CLIENT_ID,BIZ_SN,HIS_SN,
                                    NOTIFY_TIME,HIS_CONFIRM_PERIOD,HIS_CONFIRM_NAME,HIS_CONFIRM_RESULT,NOTIFY_URL,
                                    CHANNEL,CHANNEL_TYPE,YQBZ,DIRECT_PARAMS,AUTO_REFUND,LINK_COMM_SN,LINK_PAY_TYPE,
                                    EXPIRE_MINUTES,TRANS_MODE,TRANS_TXN_TYPE,BY1,BY2,BY3))
            # 提交事务
            conn.commit()
            print('{}条数据插入成功'.format(i*1000))
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        print('关闭数据库连接')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    create_test_datas()
