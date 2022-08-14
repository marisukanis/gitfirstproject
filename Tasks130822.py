"""
Task 1:
Write a program that will convert the sequence of numbers entered by
the user into text, e.g .:
112 -> "one one two"
9973 -> "nine nine seven three"

Hint: you need the input () function, a dictionary and a loop.
"""
# if __name__ == "__main__":
#     numbers = {
#         0: 'zero',
#         1: 'one',
#         2: 'two',
#         3: 'three',
#         4: 'four',
#         5: 'five',
#         6: 'six',
#         7: 'seven',
#         8: 'eight',
#         9: 'nine'
#     }
# user_input = input('give a sequence of numbers /n')
# output_str = ''
# for elem in user_input:
#     output_str += numbers[int(elem)] + ' '
# print(output_str)
"""
Task1: 
1. create a dictionary 
2. get the input
3. loop through - for x in input
4. has to be string
"""
"""
Task 2:
Create a function that takes a list of integers and returns what the
smallest number is in.
Do not use built-in functions.
eg. for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5, because
the smallest element is found at this index in this list.
"""
# #list1 = [42, 13, 56, 7, 12, 3, 85]
# def get_min_index(lst):
#     min_value = lst[0]
#     min_index = 0
#
#     for index, value in enumerate(lst):
#         if value < min_value:
#             min_value = value
#             min_index = index
#     return min_index, min_value
#
# if __name__ == '__main__':
#     int_list = [42, 13, 56, 7, 12, 3, 85]
#     index, value = get_min_index(int_list)
#     print(f'The smallest value in the list is: {value}, it is in position: {index}')

"""
Task 3:
Create a function that checks that the number given in the argument is
prime. The function should take a numeric value and return a logical
value of True / False.
E.g.- For 11 the function will return True, for 12 -> False.
"""
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(f"11: {is_prime(11)}")
    print(f"12: {is_prime(12)}")

"""
Task 4:
Create a function that checks if the string given as an argument is a
palindrome (ie reading backwards and forwards is exactly the same, eg
"kayak", "madam").
"""
def isPalindrome(s):
    return s == s[::-1]

s = 'kayak'
ans = isPalindrome(s)

if ans:
    print('yes')
else:
    print('no')

"""
Task 5:
Create a function that will calculate the number of upper and lower case
letters in a string.
eg for: "The quick Brown Fox"
expected result:
Number of uppercase letters: 3, number of lowercase letters : 13
Hint: use a loop, conditional statement, and appropriate methods for the
string.
"""
#string = 'The quick Brown Fox'
def count_upper_lower_case(sentence):
    no_upper_case, no_lower_case = 0, 0

    for char in sentence:
        if char.islower():
            no_lower_case += 1
        elif char.isupper():
            no_upper_case += 1
    return no_upper_case, no_lower_case

if __name__ == "__main__":
    string = 'The quick Brown Fox'
    upper, lower = count_upper_lower_case(string)
    print(f'Number of uppercase letters: {upper}, number of lowercase letters: {lower}')

"""
Task 6:
Write a function that takes two strings and checks to see if they are
anagrams of each other.
For example:
"Army" and "Mary",
"Sharing" and "Sunday",
"Quid est veritas?" and "Vir est qui adest",
"Jim Morrison" and "Mr. Mojo Risin"
"Tom Marvolo Riddle" and "I am Lord Voldemort"
"""
# def are_anagrams(napis1, napis2): # you can also use, for example, Counter
#     napis1 = sorted(napis1.lower().replace(" ", ""))
#     napis2 = sorted(napis2.lower().replace(" ", ""))
#     return napis1 == napis2
#
# if __name__ == "__main__":
#     print(are_anagrams("Tom Marvolo Riddle", "I am Lord Voldemort"))
#     print(are_anagrams("Ala has a cat", "Cat has Ala"))
#
# #Practice execrises:
# #Given two integer numbers return their product only if the
# # product is equal to or lower than 1000, else return their sum.
#
# def number_function(number1, number2):
#     product = number1 * number2
#     if product <= 1000:
#         return product
#     else:
#         return number1 + number2
#
# result = number_function(20, 30)
# print('The result is: ', result)
#
# result = number_function(40, 30)
# print('The result is: ', result)

#QUESTIONS:
#Q1: given 2 strings, can you make first string from
# the second by deleting some characters. Can use 'counter', intersect
s1 = "Hello"
s2 = "vufigsaiHudesdflelio"

count = 0
for ch in s1.lower():
    if ch in s2.lower():
        count += 1

    print(couny)
    if count == len(s1):
        print("Possible")
    else:
        print("Not possible")

#Q2: Sum numbers until flag -9999 is seen.
#Methods: You can save the numbers in a list and compute
# You can use while loop
# my_list2 = [10, 23.4, 67, -9999, 7, 8, 100]

# 1. You can save the numbers in a list and compute
# 2. can use positional arguments
# 3. use loop

my_list2 = [10, 23.4, 67, -9999, 7, 8, 100]
def sum_number(nums: List) -> float:
    sum = 0
    for x in nums:
        if x != -9999:
            sum += x
        else:
            break
        return sum

sum_number(my_list2)


#Q3: Find the min and max of set of numbers
# number1 = [2, 5, 7, 10]
# smallest = min(number1)
# print(smallest)
# biggest = max(number1)
# print(biggest)

def get_min_max(*args):
    return min(args), max(args)

get_min_max(12, 67, -234, -98, 100)

#Q4: Count the number of odd and even elements in a list.
# my_list = [2, 5, 7, 10]
# even_count, odd_count = 0, 0
#
# for i in my_list:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even numbers available in the list: ", even_count)
# print("Odd numbers available in the list: ", odd_count)
