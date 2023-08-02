# #02/08/23 [MYSQL]

# import mysql.connector

# conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Mithun@1730', database = 'first_database')
# my_cursor = conn.cursor()
# conn.commit()
# conn.close()

# print('Connected Successfully!!!!')

import mysql.connector

conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Mithun@1730', database = 'new')

my_cursor = conn.cursor()

# my_cursor.execute('SHOW TABLES')

# for x in my_cursor:
#     print(x)

# sql = "INSERT INTO customers(name,address) VALUES(%s,%s)"
# val = ("Naveen", "23, Anthoniyar Kovil Street, Madhagadi, Karaikal")

# my_cursor.execute(sql,val)

# conn.commit()

# print(my_cursor.rowcount,"record(s) added, ID:",my_cursor.lastrowid)

# my_cursor.execute("DROP TABLE customers") Deleting entire table

# result = my_cursor.fetchall()


# conn.commit()


# The fetchone() method will return the first row of the result

# for x in result:
#     print(x)

# my_cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),address VARCHAR(255) )")


# sql = "INSERT INTO customers (name,address) VALUES(%s,%s)"
# val = [('Mithun',"23, Anthoniyar Kovil Street Madhagadi, Karaikal"),
#        ('Naveen',"23, Anthoniyar Kovil Street Madhagadi, Karaikal"),
#        ('Morris',"23, Anthoniyar Kovil Street Madhagadi, Karaikal")
#        ]
# my_cursor.executemany(sql,val)

# conn.commit() 

# print(my_cursor.rowcount,"records added")

#  my_cursor.execute("SELECT * FROM customers WHERE address LIKE '%Kov%' ") # %___% gathers the data based on the keyword
#sql = "SELECT * FROM customers WHERE address = %s"     ###### Prevents SQL Injections  ######
#val = ('23, Anthoniyar Kovil Street Madhagadi, Karaikal',)

sql = "SELECT * FROM customers WHERE address ORDER BY name DESC"
my_cursor.execute(sql)
result = my_cursor.fetchall()
# my_cursor.execute("UPDATE customers SET address = '25, Anthnoiyar Kovil Street, Madhagadi, Neravy Post, Karaikal' WHERE id = 3 ")
# result = my_cursor.fetchall()
# conn.commit()
# print(my_cursor.rowcount,"record(s) updated....")

for x in result:
    print(x)

# conn.commit() -> is required to make the changes, otherwise no changes are made to the table.