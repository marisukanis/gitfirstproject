"""
Object-oriented programming is the use of objects/classes.
Object has properties and methods.
    An object is an instance of a class.

Class is a blueprint for creating objects
Advantages of OOP:
- help you bundle functionalities together
- easy creation of a class instance {object}
- ability to modify methods of a class without changing the class
- allows you to create user-defined data structure

Examples:
class: car:
- minimum size - maximum size
- 4 tyres/wheels
- windows and windshields
- headlamps
- maximum and minimum seating
- steering wheel

objects: different types of cars:
- Hyundai, Subaru, Toyota, Mercedes, Tesla, Volvo

class: Students:
- Cohort
- Course
- Location
- Method (remote/physical)

objects: Data Science1, Data Science2, Data Science PH, Python

Structure:
class <<Class_name>>: class name should start with Capital Letter
    pass

Class has methods - functions defined in the body of the class.
    First argument in the function is {self}
    has attributes - variables defined in a class

__init__ - function/constructor - place, where your class starts

- num of doors
- max speed
- max passengers
- name

Method structure:
def <<method_name>>(self, <<any_parameter):
    pass

Instance variables are for data unique to each instance
class variables are for attributes and methods shares
by all instances of the class
"""
class Car:
    accelerate = 15 # this is a class variable
    def __init__(self, name, num_doors=4, exotic=False):  #constructor
        self.name = name
        self.door_no = num_doors
        self.is_exotic = exotic
        self.in_motion = False
        self.speed = 0

    def get_doors(self):
        if self.door_no not in [2, 3, 4]:
            return f"{self.name} has invalid door numbers"
        return self.door_no

    def drive(self):
        self.in_motion = True

    def acceleration(self, acceleration=10):
        if self.in_motion:
            self.speed += self.accelerate

    def stop(self):
        self.in_motion = False


car1 = Car(name="Toyota Prius", num_doors=4)
car2 = Car(name="Tesla A20", num_doors=2, exotic=True)
print(car1)
car2.drive()
car2.acceleration()
car2.acceleration()

car1.drive()
car1.acceleration()
#result: <__main__.Car object at 0x7fd2f01a0fd0>
print(car1.speed)
print(car2.speed)

car1.speed = 500
print(car1.speed)
