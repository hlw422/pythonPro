# coding: utf-8
# 批量生成测试数据,并保存到mysql
from faker import Faker
import pymysql
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
        sql = "INSERT INTO `user` (`dept_id`, `user_name`, `nick_name`, `user_type`, `email`, `phonenumber`, `sex`, `avatar`, `password`, `status`, `del_flag`, `login_ip`, `login_date`, `create_by`, `create_time`, `update_by`, `update_time`, `remark`) VALUES (%s, %s, %s, %s, %s, %s, '1', '', '$2a$10$7JB720yubVSZvUI0rEqK/.VqGOZTH.ulu33dHOiBE8ByOhJIrdAu2', '0', '0', '127.0.0.1', '2022-01-30 12:55:06', 'admin', '2022-01-30 12:35:45', '', '2022-01-30 12:55:06', '管理员');"  # 创建一个sql语句
        # 循环生成数据
        for i in range(1, 1000):
            for j in range(1000):
                # 生成数据
                dept_id = fake.random_int(min=1, max=100)
                name = 1
                nick_name = fake.name()
                user_type = fake.random_int(min=1, max=2)
                email = fake.email()
                phonenumber = fake.phone_number()
                # 执行sql语句
                cursor.execute(sql, (dept_id,name,nick_name,user_type,email,phonenumber))
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
