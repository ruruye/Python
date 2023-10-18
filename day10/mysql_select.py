import pymysql
 
conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', port=3304, charset='utf8')
 
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from emp"
curs.execute(sql)
 
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()