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


def starrocksInsertSql():
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
    starrocksInsertSql()
    end_time = datetime.now()
    print("结束时间：", end_time)
    print('定制化需求耗时：', end_time - start_time)
