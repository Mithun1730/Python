#01/08/23

# # class Person:
# #     def __init__(self,name,age):
# #         self.fullname = name
# #         self.currentage = age
        
# #     def __str__(self):
# #         return f'{self.fullname}({self.currentage})'
        
# # p2 = Person('Mithun',23)
# # print(p2)
 
# # class StudentDetails:   #Parent Class
# #     def __init__(self,name,dept):
# #         self.fullname = name
# #         self.deptname = dept
# #     def myfunc(self):
# #         print(f'{self.fullname} {self.deptname}')
        


# # class Teacher(StudentDetails):   #Child Class
# #     def __init__(self, name, dept,year):
# #         super().__init__(name, dept)
# #         self.graduationyear = year
        
# #     def welcome(self):
# #         print(self.fullname,self.deptname,self.graduationyear)

# # x1 = StudentDetails("Mithun",'Chemistry',3030)
# # x1.welcome()

        
        
        
        
     
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()


class Bus:
    def __init__(self,name,far):
        self.busname = name
        self.farperhead = far

class Timing(Bus):
  def __init__(self, name, far, hours):
     super().__init__(name, far)
     self.totalhours = hours
  
  def welcome(self):
      print('{0} will take {2} hours to reach Pondicherry with a far amount of {1}' .format(self.busname, self.farperhead, self.totalhours))

x = Timing('PRTC',125,4)
x.welcome()

    
        