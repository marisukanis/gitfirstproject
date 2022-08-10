Assignment: Revision for Numeric, String and Sequence Data Types
Due date is May 14


read function range()
https://docs.python.org/3/library/stdtypes.html#range


Reverse the order of words in a given sentence.



str_val = "Hello World"
output = "World Hello"



Write a program  that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

hint: use set() =>

list1 = [10, 23, 23, 5, 67, 10]
output = [10, 23, 5, 67]



Write a password strength verifier in Python that checks if user password is strong.
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.


password = 'food'
result = False

password = '1EggPerD@y'
result = True



Write a program to reverse row sort in list of lists


list_id = [[4,1,6], [7,9], [8,9,2,4]]
result = [[6,4,1], [9,7], [9,8,4,2]]



Write a program to pair elements with rear element in matrix row


list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
result = [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]



Replace each special symbol with # in the following string
Hint: import string, and use string.punctuation



import string
string.punctuation



str1 = "%There &are three( students$ and& 1 trainer!"
result = "#There #are three# students# and# 1 trainer#"



Remove all characters for string except integers
hint: list comprehension and isdigit()



str1 = "My mum has a 10 year old dog and 2 fishes"
result = 102



Remove all empty strings from a list of strings
hint: use filter() => https://docs.python.org/3/library/functions.html#filter



name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']