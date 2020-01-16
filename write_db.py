import pymysql

# 创建数据库连接
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", database="stu", charset="utf8")

# 生成游标对象(操作数据库,执行sql语句,获取结果)
cur = db.cursor()

# 写操作
try:
    # sql = "insert into cls (name,age,score) values (%s,%s,%s)"
    # cur.execute(sql, ["Tom", 16, 54])
    # db.commit()
    sql = "updata cls set='m' where name='Jame';"
    cur.execute(sql)

    sql = "delete from cls where sex is null;"
    cur.execute(sql)

    db.commit()
except Exception:
    db.rollback()

# 关闭游标和数据库连接
cur.close()
db.close()
