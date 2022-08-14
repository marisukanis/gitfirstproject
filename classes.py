"""
CLASS METHOD:
    - called on the class itself, not on an object instance
    - can only access your class variables
    - takes the first argument as a class 'cls'
    <<class>>.<<class_method>>
"""

"""
STATIC METHOD:
    - general utility methods that perform tasks in isolation
    - don't take 'self' or 'cls' parameters
    - bound to class but not the object of the class
    
ACCESS RESTRICTIONS:
- private: only accessible within the class
- public is accessible everywhere: within the class, inheritance, objects
"""

class Student:
    study_type = "remote"
    def __init__(self, name, age, cohort):
        self.name = name
        self.age = age
        self.__cohort = cohort

    def print_std(self):
        print(f"name: {self.name}\nage: {self.age}\nstudy type: {self.study_type}\ncohort: {self.__cohort}")

    def __myprivate_var(self):
        print("I am private")

    @classmethod #function inside a function, acts as decorator, classmethod is 'cls'
    def set_study_type(cls, mode):
        cls.study_type = mode

    @staticmethod
    def is_weekend(day):
        return day in [5, 6]

    @staticmethod
    def sample_std():
        print(f"name: sample\nage: sample age\nstudy type: hybrid")

std1 =  Student("name", 28, "DS1")
std1.print_std()

#print(std1.cohort)

Student.set_study_type("Hybrid") # this is how you call a class method

std1.print_std()
Student.sample_std()
std1.sample_std()
