from typing import List, Optional, Union

"""
Clean code rules:
    - correct function names describe what the function does
    - documentation: doc string
    - type annotation: type hinting, type of data
        Union = a or b or c
        Optional = a or None
    - single responsibility of functions and classes (your func and class should only do 1 thing)
    
PEP8 - style guide:
    - indentation 4
    - 2 blank spaces between functions outside class
    - 1 blank space between methods inside class
    - 1 space
    - last line of your file should be empty/blank
    - line length - max 98
    - imports should be at the top + alphabetical
    - etc.
"""
def convert_to_celcius(farheit: Union[float, int]) -> float: #hinting the type
     return (farheit - 32) * 5/9

convert_to_celcius('4')

def welcome_to_class(name: str) -> None:
    print('Welcome')

class Calculator:
    """
    A class that simulates the scientific calculator

    :parameters
    number - an integer that you want to perform action on
    default value = 0 (if there is default)

    :methods
    - add
    """
    def __init__(self, number: float = 0) -> None:
        self.number = number
        self.rst = 0

    def __add__(self, num = 0) -> 'Calculator':
        self.rst += num
        return self

    #TODO: add method multiply and subtract

class AWSConnection:
    pass

cal = Calculator()

def get_active_account(user_id: str = None) -> List:
    """
    :param user_id:
    :return: List
    """
    acct = []
    if user_id == None:
        return acct   #returns list of all active accounts
    acct.append(user_id)
    return acct    #returns just 1 user active account

def get_account_info(user_id):
    pass
