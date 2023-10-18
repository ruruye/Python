import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', port=3304, charset='utf8')


curs = conn.cursor()
e_id = "3"

sql = f"""
DELETE FROM emp 
WHERE 
    e_id='{e_id}'
"""

cnt = curs.execute(sql)
print("cnt:", cnt)

conn.commit()

curs.close()
conn.close()