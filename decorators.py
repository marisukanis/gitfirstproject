"""
In python you can:
 - create a function inside another function
 - pass a function as an argument to another function
 - a function can return another function
A decorator is a function that takes another function
and extends the behaviour of the latter function
without explicitly modifying it
"""
#example:
def increment_num(num):
    return num + 2
print(increment_num(3))

"""Using a function as argument"""
def welcome_student(name):
    return f'Welcome {name} from the break'

def did_you_study(name):
    return f'I hope you studied and revised python {name}'

def greetings(any_func): #function as an argument in another function
    return any_func('Maris')
print(greetings(did_you_study))
print(greetings(welcome_student))

"""
create a function inside another function - nested functions:
    - inner functions are not defined until the parent 
    function is called
    - can't be called without the parent func called
    - inner function is local to your function, hence 
    they are not available outside the parent
"""
def outer_box():    #parent function
    print('This is the parent box')

    def middle_box():   #inner function
        print('This is the middle box')

    def last_box():     #inner function
        print('This is the last one'.upper())

    middle_box()
    last_box()
outer_box()

"""function returning another function"""
def greeting(hour):
    def morning(name):
        return f'Good morning {name}'
    def afternoon(name):
        return f'Good afternoon {name}'
    def evening(name):
        return f'Good evening {name}'
    def night(name):
        return f'Good night {name}'

    if hour < 12: #0-11
        return morning
    elif hour >= 12 and hour <= 17:
        return afternoon
    elif hour >= 17 and hour < 20:
        return evening
    else:
        return night

greet = greeting(21)
print(greet('Maris'))

"""
decorator:
    - takes a function as an argument
    - defines an inner function
    - returns the function as the result of its operation
"""

def my_decorator(func):     #takes a function as an argument
    def wrapper():      #defines an inner function
        print(f'This is my wrapper')
        func()
    return wrapper  #returns the function as the result of its operation

def say_cheese():
    print('Python is fun!!')

say_cheese()
my_decorator(say_cheese)()  #pass in the () function for wrapper

@my_decorator
def say_something():
    print('saying something')

say_something()

# *args - named arguments
# **kwargs - non-named arguments

def increment(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@increment
def just_a_num(num):
    return num + 3
@increment
def two_nums(num1, num2):
    return num1+3, num2+3

print(just_a_num(5))
print(two_nums(10, 8))

"""
*args, positional arguments
    a, b, c = (10, 3, 6) 

**kwargs - accepts named arguments
    num1 = 3, num2 = 10, num3 = 6
    
in Python positional comes before named argument (e.g. *args before **kwargs)
"""
def some_example(val1, val2, val3):
    print(val1)
    print(val2)
    print(val3)
    print('doing something')
some_example(10, 3, 7)  #positional argument
some_example(val2=10, val3=6, val1=8)   #named argument
some_example(8, 7, val3=17)

def some_example(*args):
   for x in args:
    print(x)
some_example(10, 3, 7)  #positional argument
some_example(2, 3, 4, 5, 6, 7, 7)
#some_example(val2=10, val3=6, val1=8)   #named argument
#some_example(8, 7, val3=17)