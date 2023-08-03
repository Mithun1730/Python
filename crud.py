#03/08/23
import mysql.connector

conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Mithun@1730', database = 'employee')

my_cursor = conn.cursor()

#### CREATE DATABASE ######

my_cursor.execute("CREATE DATABASE employee")
my_cursor.execute('SHOW DATABASES')

##### CREATE TABLE #####

my_cursor.execute("CREATE TABLE details (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), address VARCHAR(255), designation VARCHAR(255))")
# my_cursor.execute("SHOW TABLES")

print("TABLE CREATED successfully...")


##### INSERT DATA #####

sql = "INSERT INTO details (name, email, address, designation) VALUES (%s,%s,%s,%s)"
val = [('Mithun', 'mitchellmithun@gmail.com', '23, Anthoniyar Kovil Street, Madhagadi, Karaikal', 'Trainee'),
       ('Naveen', 'naveensharma45@gmail.com','232/A, Church Street, Karaikal', 'Web Developer'),
       ('Morris', 'chrismorris077@gmail.com', '12, Anna Salai, Chennai', 'Trainee'),
       ('Chandru', 'chandru0321@gmail.com', '77, Bussy Street, White Town, Puducherry', 'Trainee'),
       ('Arjun', 'mitchellmithun@gmail.com', '18/1, P.K Salai, Karaikal', 'Trainee')]

my_cursor.executemany(sql,val)
conn.commit()
print(my_cursor.rowcount,'record(s) inserted successfully')

##### READ DATA #####

my_cursor.execute("SELECT * FROM details")
result = my_cursor.fetchall()
for x in result:
    print(x)


##### UPDATE DATA #####

sql = "UPDATE details SET designation = 'Developer' WHERE  designation = 'Trainee' "
my_cursor.execute(sql)
conn.commit()
print(my_cursor.rowcount,"record(s) updated successfully")

##### UPDATE DATA [READ] #####

my_cursor.execute("SELECT * FROM details")
result = my_cursor.fetchall()
for x in result:
    print(x)


##### DELETE DATA #####

sql = " DELETE FROM details WHERE designation = 'Web Developer' "
my_cursor.execute(sql)
conn.commit()
print(my_cursor.rowcount,'record(s) deleted successfully...')

##### AFTER DELETION [READ] #####

my_cursor.execute("SELECT * FROM details")
result = my_cursor.fetchall()
for x in result:
    print(x)
