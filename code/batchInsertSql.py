import mysql.connector

# 创建数据库连接
cnx = mysql.connector.connect(user='your_username', password='your_password', host='localhost', database='your_database')

# 创建游标对象
cursor = cnx.cursor()

# 从文件中读取 INSERT 语句
with open('insert_statements.sql', 'r') as file:
    insert_statements = file.read().split(';')[:-1]  # 去掉最后一条空语句

# 开始事务
cnx.start_transaction()

# 逐一执行 INSERT 语句
for insert_statement in insert_statements:
    try:
        cursor.execute(insert_statement)
    except mysql.connector.Error as err:
        print(f"执行 INSERT 语句时出错: {err}")
        cnx.rollback()  # 回滚事务
        break

# 提交事务或回滚事务
if cursor.rowcount == len(insert_statements):
    cnx.commit()
    print("事务已提交")
else:
    cnx.rollback()
    print("事务已回滚")


# 关闭游标和数据库连接
cursor.close()
cnx.close()
