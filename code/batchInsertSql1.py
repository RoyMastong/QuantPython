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
import mysql.connector
import pymysql
import jaydebeapi
import time




import scipy.stats as stats

import scipy.optimize as opt

# 数据库连接方式2
user = STARROCKS_MYSQL_DW.get('user')
password = STARROCKS_MYSQL_DW.get('password')
pwd = parse.quote_plus(password)  # 密码中有特殊符号@,需要转换一下
host = STARROCKS_MYSQL_DW.get('host')
port = STARROCKS_MYSQL_DW.get('port')
database = STARROCKS_MYSQL_DW.get('db')
db_connection_str = f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{database}'

def querySql():
    # 查询语句
    sql = """
    select * from tags_eu limit 1;
    """
    df = pd.read_sql(sql, db_connection_str)
    print(df)
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
    conn = pymysql.connect(host=host,
                           user=user,
                           password=pwd,
                           db=database,
                           port=9030,
                           charset='utf8')

    # 创建游标对象
    cursor = conn.cursor()

    # 从文件中读取 INSERT 语句
    with open('/Users/junqi.chen/20230424insertTag.sql', 'r') as file:
        insert_statements = file.read().split(';')[:-1]  # 去掉最后一条空语句

    # 开始事务
    cursor.execute("START TRANSACTION")

    # 每500条执行 INSERT 语句1
    # for i in range(0, len(insert_statements), 500):
    #     try:
    #         cursor.execute("".join(insert_statements[i:i + 500]))
    #         print("执行成功", insert_statements[i:i + 500])
    #     except pymysql.Error as err:
    #         print(f"执行 INSERT 语句时出错: {err}", insert_statements[i:i + 500])
    #         cursor.execute("ROLLBACK")


    # 逐一执行 INSERT 语句
    # for insert_statement in insert_statements:
    #     try:
    #         cursor.execute(insert_statement)
    #         print("执行成功", insert_statement)
    #     except pymysql.Error as err:
    #         print(f"执行 INSERT 语句时出错: {err}", insert_statement)
    #         cursor.execute("ROLLBACK")  # 回滚事务
    #         break
    #
    # # 提交事务或回滚事务
    # if cursor.rowcount == len(insert_statements):
    #     cursor.execute("COMMIT")
    #     print("事务已提交")
    # else:
    #     cursor.execute("ROLLBACK")
    #     print("事务已回滚")

    for i, insert_statement in enumerate(insert_statements):
        try:
            cursor.execute(insert_statement)
            print("执行成功", insert_statement)
        except pymysql.Error as err:
            print(f"执行 INSERT 语句时出错: {err}", insert_statement)
            cursor.execute("ROLLBACK")  # 回滚事务
            break

        # 每500条数据提交一次并休息一段时间
        if i % 500 == 0 and i > 0:
            time.sleep(120)  # 休息2分钟
            cursor.execute("START TRANSACTION")

    # 最后提交事务
    cursor.execute("COMMIT")
    print("事务已提交")

    # 打印结果
    print("success!")

    # 关闭游标和连接
    cursor.close()
    conn.close()



if __name__ == '__main__':
    start_time = datetime.now()
    print("开始时间：", start_time)
    sql1()
    end_time = datetime.now()
    print("结束时间：", end_time)
    print('定制化需求耗时：', end_time - start_time)