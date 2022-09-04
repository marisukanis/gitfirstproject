"""
Task 1:
Write a program that will convert the sequence of numbers entered by
the user into text, e.g .:
112 -> "one one two"
9973 -> "nine nine seven three"

Hint: you need the input () function, a dictionary and a loop.
"""
# my_dict = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
#     0: 'zero'}
#
# key = input('Insert number: ')
# output = ''
#
# for i in key:
#     output += my_dict[int(i)] + ' '
# print(output)

"""
Task 2:
Create a function that takes a list of integers and returns what the
smallest number is in.
Do not use built-in functions.
eg. for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5, because
the smallest element is found at this index in this list.
"""

my_lists = [42, 13, 56, 7, 12, 3, 85]

my_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: 'zero'}

for key in my_dict:
    value = my_dict[key]
    # print(f'{key} -> {value}')
    print(value)



