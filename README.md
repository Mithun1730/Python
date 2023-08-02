# Python
DAY 1 - 01/08/2023
1) Classes & Objects
class MyClass:
    x = 5 #property
p1 = MyClass() #object

self - The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class

eg:
class Details:
  def __init__(newobject,a,b)
    newobject.a = a
    newobject.b = b
  def myfunc(abc)  
    print("Hello" + abc.a)

x1 = Details(Mithun, 45)
x1.myfunc()

i) Learning Python MYSQL  ## 02/08/2023

***Connection***
 cursor() -> The MySQLCursor of mysql-connector-python (and similar libraries) is used to execute statements to communicate with the MySQL database.

 mydb.commit() -> is required to make the changes, otherwise no changes are made to the table.

 *** INSERT, UPDATE, DELETE, ORDERBY, SELECT, JOINS ***

//Inner Join -> INNER JOIN only shows the records where there is a match.

//Left Join -> If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement

 * 


