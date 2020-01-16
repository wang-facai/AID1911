# import pymysql
#
# db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", database="dict", charset="utf8")
#
# cur = db.cursor()
#
# f_r = open("dict.txt", "r")
# while True:
#     data = f_r.readline()
#     if not data:
#         break
#     word = data.split(" ", 1)[0]
#     mean = data.split(" ", 1)[-1].strip()
#     print("%s---%s" % (word, mean))
#
#     sql = "insert into words (word,mean) values (%s,%s)"
#     try:
#         cur.execute (sql, [word, mean])
#     except Exception as e:
#         print(e)
#         db.rollback()
# db.commit()
#
# cur.close()
# db.close()

import re

import pymysql

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", database="dict", charset="utf8")

cur = db.cursor()

f_r = open("dict.txt", "r")
args_list = []
for line in f_r:
    l = re.findall(r"(\w+)\s+(.*)",line)
    print(l)
    args_list.extend(l)
sql = "insert into words (word,mean) values (%s,%s)"
try:
    cur.executemany(sql, args_list)
    db.commit()
except:
    db.rollback()


cur.close()
db.close()
