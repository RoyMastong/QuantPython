import math
import pandas as pd
import numpy
from config import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import load_workbook
import pylab as pl
import pymysql
from urllib import parse
from datetime import datetime
import numpy as np
import sqlalchemy
# import mysql.connector
import pymysql


import scipy.stats as stats

import scipy.optimize as opt

# 数据库连接方式2
user = UCLS_MYSQL_DW.get('user')
password = UCLS_MYSQL_DW.get('password')
pwd = parse.quote_plus(password)  # 密码中有特殊符号@,需要转换一下
host = UCLS_MYSQL_DW.get('host')
port = UCLS_MYSQL_DW.get('port')
database = UCLS_MYSQL_DW.get('db')
db_connection_str = f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{database}'

def querySql():
    # 查询语句
    sql = """
    select * from tags limit 1;
    """
    df = pd.read_sql(sql, db_connection_str)
    print("success！")


# def excuteSql():
#
#     # 建立数据库连接
#     mydb = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=pwd,
#         database=database
#     )
#
#     # 获取游标对象
#     mycursor = mydb.cursor()
#
#     # 定义Insert语句列表
#     insert_statements = [
#         "insert into tags_eu (id, name, level, parent_id, deleted, is_active, create_by, create_time, last_update_by, last_update_time, attribute_id, max_readvolume, user_impact, score, code, source, source_tag_id, cn_name, ufp_code, category) values  (23565, 'cai0241cieshiyonghusuqiu', 4, 23563, 0, 1, null, '2023-04-21 08:33:21', null, '2023-04-21 08:33:21', null, null, null, null, null, 'IPD+', 'UREQ004213', 'cai0421测试用户诉求', 'IPDP1682066000528', 'PRODUCT_EXPERIENCE')"
#         # ...添加更多Insert语句...
#     ]
#
#     # 循环执行Insert语句
#     for statement in insert_statements:
#         mycursor.execute(statement)
#
#     # 提交更改
#     mydb.commit()
#
#     # 关闭数据库连接
#     mydb.close()


def sql1():
    # 连接数据库
    conn = pymysql.connect(host=host,
                           user=user,
                           password=pwd,
                           db=database,
                           charset='utf8')

    # 创建游标对象
    cursor = conn.cursor()

    # 执行 SQL 查询
    cursor.execute("SELECT * FROM tags_eu limit 1")

    # 获取查询结果
    result = cursor.fetchall()

    # 打印结果
    print(result)

    # 关闭游标和连接
    cursor.close()
    conn.close()




if __name__ == '__main__':
    start_time = datetime.now()
    print("开始时间：", start_time)
    querySql()
    # excuteSql()
    # sql1()
    end_time = datetime.now()
    print("结束时间：", end_time)
    print('定制化需求耗时：', end_time - start_time)