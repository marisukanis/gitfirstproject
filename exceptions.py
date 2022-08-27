"""
Errors terminates the python code been executed
    - syntax error / parser error
        - shows the error with ^
        - most IDE catches this error
    - exceptions: errors that occur during execution
        - code is syntactically correct
        - but error occurs when you try to execute your code

exception handling:
Try: block of code that might generate error / run this code
except: handle the exception
else: executes the code when there is no error
finally: executes whether an error occurs or not
"""
#1exem = 10  - syntax error: against python rules
#print('learning error', 1name) - syntax error
# try:
#     print(10/0)     #exception error
# except:
#     print('do nothing')
#
# try:
#     x = 10
#     y = [10, 3, 2, 0, 4, 6]
#     z = [x/m for m in y]
# except:
#     print('ran into an error')

#else + finally
# try:
#     print(10/2)     #exception error
# except:
#     print('do nothing')
# else:
#     print('No error')
# finally:
#     print('I occur regardless of an error')

"""Example: database connection:
try: make a connection
except: error
finally: close the connection

Read and write to a file:
try: read the file
    write to a file
except: error that occurs during reading of the file
finally/else: close the file
"""
"""Types of Exceptions:
- Arithmetic error: ZerodivisionError e.g. 10/0
                    OverflowError
- Assertion error: when assertion fails
- EOF error (end of file error)
- Import error e.g. 'from module import JustSayingSomething'
- ModuleNotFound error
- Index error, e.g. 'list1 = [12, 4, 5, 6]
                     list1[7]'
- Key error (dictionary) - can not find key in dict
- Name error - when your variable name can not be found
"""
"""Multiple Exceptions"""
# try:
#     print(name)
# except NameError as err:     #named exceptions
#     msg = err
#     print(f'a new message: {err}')
# except:
#     print('other errors')

"""Creating Customized Exceptions"""
# class NoNegativeInList(Exception):
#     pass

"""Raise Exceptions"""
# list1 = [10, 4, 5, 6, -1, 7, 7]
# for x in list1:
#     if x < 0:
#         raise NoNegativeInList('Negative values should not be in the list')
#

"""
Task 10:
Write a program that returns the absolute value of a number retrieved
from the user. The program should keep asking for this number until it is
correctly given.
Remember that the user may not always enter a numeric value, but may
also enter, for example, "cauliflower". Check what happens then and be
sure to handle exceptions.
"""
if __name__ == "__main__":
    while True:
        try:
            number = float(input('Enter a number: '))
            print(f'The absolute value of {number} is {abs(number)}')
            break
        except ValueError:
            print('Cannot return absolute value for the specified input')


