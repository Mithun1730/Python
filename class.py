class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'{self.name}({self.age})'
        
p2 = Person('Mithun',23)
print(p2)
        
        
     
        