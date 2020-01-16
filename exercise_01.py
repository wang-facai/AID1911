import pymysql

# 创建数据库连接
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", database="stu", charset="utf8")

# 生成游标对象(操作数据库,执行sql语句,获取结果)
cur = db.cursor()

# 读操作
# name = input("学生姓名:")
# sql = "select name,hobby,price from interest where name = '%s';" % name
# sql = "select name,hobby,price from interest where name = %s;"
sql = 'select name,age,score from cls where score>%s and age>=%s;'

cur.execute(sql, [80, 18])  # 执行sql语句,通过参数列表给sql语句传入值

all_row = cur.fetchall()  # 获取所有记录

print(all_row)

# 关闭游标和数据库连接
cur.close()
db.close()
