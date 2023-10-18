import pymysql
 
conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', port=3304, charset='utf8')



curs = conn.cursor()
e_id="4"
e_name="4"
gen="4"
addr="4"

sql = f"""
INSERT INTO emp 
    (e_id, e_name, gen, addr)  
VALUES 
    ('{e_id}','{e_name}', '{gen}', '{addr}')
"""


cnt = curs.execute(sql)
print("cnt", cnt)

print("curs.rowcount", curs.rowcount)

conn.commit()

curs.close()
conn.close()