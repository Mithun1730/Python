class Details:
    def __init__(self,name,age):
        self.firstname = name
        self.currentage = age
class New(Details):
    def __init__(self, name, age, place):
        super().__init__(name, age)
        self.location = place
    def result(self):
        print("{0} ({1}) ____from____{2}".format(self.firstname,self.currentage,self.location))
        
x1 = New('Mithun',23,'Karaikal')
x1.result()
        
        