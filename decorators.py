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
