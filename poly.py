#01/08/23
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Drive!")

# class Bike:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Ride!")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Sail!")
        
# car1 = Car('Ford',2022)
# bike1 = Bike('Ducati',2022)
# boat1 = Boat('Yamaha',2000)

# for x in (car1,bike1,boat1):
#     x.move()
        
        
        
#### polymorphism with inheritance

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print('Move! - [DEFAULT]')

class Car(Vehicle):
    def move(self):
        print('Drive!')
class Bike(Vehicle):
    def move(self):
        print('Ride!')
class Plane(Vehicle):
    def move(self):
        print("Fly!")
        
class Truck(Vehicle):
    pass

car1 = Car('Ford','Mustang')
bike1 = Bike('Honda','Shine')
plane1= Plane('Emirates','766666EM')
truck1 = Truck('Ford','Mustang')

for x in (car1, bike1, plane1, truck1):
    print(x.brand)
    print(x.model)
    x.move()
    print("\n")
