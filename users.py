import mysql.connector
conn = mysql.connector.connect(host = 'localhost',user = 'root', password = 'Mithun@1730', database = 'users')

my_cursor = conn.cursor()
# sql = "INSERT INTO users (name,fav) VALUES(%s,%s)"
# val = [('Chandru','')]
# my_cursor.executemany(sql,val)
# conn.commit()
# print(my_cursor.rowcount,'record(s) inserted...')
sql = "SELECT users.name AS user, \
        products.pname AS favourite \
            FROM users \
            LEFT JOIN products ON users.fav = products.id"
my_cursor.execute(sql)
result = my_cursor.fetchall()

for x in result:
    print(x)

