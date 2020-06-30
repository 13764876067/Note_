#coding:utf-8

'''

1.python 中的sql操作部分

sqlite数据库
    增,删,查,除,创建

mysql数据库
    增,删,查,除,创建

'''

'''

1.sqlite数据库的读写
    sqlite是小型关系型数据
    python内置驱动模块
    类似文件操作一样
    本地文件
    
    创建数据库和写操作:
        1.连接数据库
        2.创建conn游标
        3.编写数据库sql
        4.执行sql语句
        5.commit提交执行
        6.关闭连接close
    读操作:
        1.连接数据库
        2.创建conn游标
        3.编写数据库sql
        4.执行sql语句
        5.result获取数据集结果    
        6.关闭连接close
        
3.mysql数据库的操作

    连接模块:
        mysql-connector-python
        MySQL-python
        PyMySQL
        
        pip install mysql-connector-python

    python DB-API:
        引入模块
        获取与数据库的连接
        执行sql语句和存储过程
        关闭连接
        
        针对事务机制的方法
        commit():提交
        rollback():回滚
        
        cursor()方法:游标
            操作mysql方法:
                callproc()
                execute():执行sql
                executemany():执行sql,重复执行参数列表里的参数
                next():移动到下一个结果集
                
            接受返回值方法:    
                fetchall():接受全部返回值
                fetchmany():带参数接受指定的条数返回结果
                fetchone():返回一条结果
                rowcount:返回执行exectue()方法后影响的行数
                scroll():移动到某一行,mode='relative':从当前行移动多少条,mode='absolute':从结果集第一行移动多少条
    
    mysql数据库
        开源(社区版),Oracle公司
        大型的数据库
        标准的sql语言形式
        运行多个系统之上,多种语言
        可以定制,采用GPL协议,可修改源代码为自己的sql
        
        基本组成:
            mysql服务器:存数据
            mysql客户端程序:用于连接操作mysql服务器
    
    python基本读写mysql
        创建数据库和写操作:
            1.连接数据库 connector.connect()
            2.创建conn游标 connection.cursor()
            3.编写数据库sql write_sql
            4.执行sql语句 cursor.execute(sql)
            5.commit提交执行 cursor.commit()
            6.关闭连接close cursor.close(),connection.close()
        读操作:
            1.连接数据库 connector.connect()
            2.创建conn游标 connection.cursor()
            3.编写数据库sql select_sql
            4.执行sql语句 cursor.execute(sql)
            5.result获取数据集结果 cursor.fetchall()  
            6.关闭连接close cursor.close(),connection.close()

'''

print('---------------------------------------------数据库sqlite操作-----------------------------------------------------')

'''
import sqlite3

conn = sqlite3.connect('./sqlitedb/sm_app.sqlite')
cour = conn.coursor()
create_users_table = """
CREATE TABLE IF NOT EXISTS user_info(
id INTEGER PREPARE KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER ,
gender TEXT
);
"""
cour.execute(create_users_table)

create_users = """
INSERT INTO
user_info (name,age,gender)
VALUES 
('lucy',20,'male'),
('bob',20,'female'),
('john',20,'male');
"""
cour.execute(create_users)
conn.commit()

select_user = """
SELECT * FROM user_info;
"""
cour.execute(select_user)
result = cour.fetchall()

cour.close()
conn.close()
'''

print('---------------------------------------------数据库sqlite操作-----------------------------------------------------')

print('---------------------------------------------数据库mysql操作-----------------------------------------------------')

import mysql.connector
from mysql.connector import Error

'''
#连接mysql
def create_connection(host_name,user_name,user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print('connection to mysq successful!')
    except Error as e:
        print(f"The erro '{e}' occurred")
    return connection

#建立连接
connection = create_connection('localhost','root','1010')

#创建数据库
def create_db(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("db create successful")
    except Error as e:
        print(f"The erro '{e}' occurred")
#创建
create_db_query = "CREATE DATABASE reader;"
create_db(connection,create_db_query)
'''

#连接mysql
def create_connection(host_name,user_name,user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print('connection to mysq successful!')
    except Error as e:
        print(f"The erro '{e}' occurred")
    return connection

#建表,即:写
def execute_query(connection,query):
    cusor = connection.cursor()
    try:
        cusor.execute(query)
        connection.commit()
        print('query execute has successful')
        cusor.close()
    except Error as e:
        print(f"The erro '{e}' occurred")

# 读操作
def execute_read_query(connection,query):
    cusor = connection.cursor()
    result = None
    try:
        cusor.execute(query)
        result = cusor.fetchall()
        print('read-query execute has successful')
        cusor.close()
        return result
    except Error as e:
        print(f"The erro '{e}' occurred")

#建表
create_user_table="""
CREATE TABLE IF NOT EXISTS user_info(
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL,
    age INT ,
    gender TEXT,
    PRIMARY  KEY (id)
) ENGINE=InnoDB;
"""

#插入语句
create_users = """
INSERT INTO
`user_info` (`name`,`age`,`gender`)
VALUES 
('lucy',20,'male'),
('bob',20,'female'),
('john',20,'male');
"""

#读操作
select_user = """
SELECT * FROM user_info;
"""

#建立连接
connection = create_connection('localhost','root','1010','reader')
execute_query(connection,create_user_table)
execute_query(connection,create_users)
result = execute_read_query(connection,select_user)
print(result)

#关闭连接
connection.close()

print('---------------------------------------------数据库mysql操作-----------------------------------------------------')