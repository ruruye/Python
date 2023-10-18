import pymysql
 
conn = pymysql.connect(host='127.0.0.1', user='root', password='python',
                       db='python', port=3304, charset='utf8')



curs = conn.cursor()

sql = """
INSERT INTO emp 
    (e_id, e_name, gen, addr)  
VALUES 
    (%s, %s, %s, %s)
"""

my_tup = ("3", "3", "3", "3")

curs.execute(sql, my_tup)
conn.commit()

curs.close()
conn.close()