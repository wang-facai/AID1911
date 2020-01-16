import pymysql

list_ = [("Dave", 17, "m", 81), ("Ala", 18, "w", 84), ("Eva", 19, "w", 91), ]

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", database="stu", charset="utf8")

cur = db.cursor()
sql = "insert into cls (name,age,sex,score) values (%s,%s,%s,%s);"
try:
    # for i in list_:
    #     cur.execute(sql, i)
    cur.executemany(sql, list_)
    db.commit()
except:
    db.rollback()

cur.close()
db.close()


