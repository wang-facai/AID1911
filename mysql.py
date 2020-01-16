"""pymysql的基本流程"""
import pymysql

# 创建数据库连接
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", database="stu", charset="utf8")

# 生成游标对象(操作数据库,执行sql语句,获取结果)
cur = db.cursor()

# 执行sql各种操作


# 关闭游标和数据库连接
cur.close()
db.close()
