""""
String Exercises
"""

#1. Write a program to create a new string made of the middle three characters
#of an input string.

#Example
input = 'JhonDipPeta'
#result = Dip
print(input[4:7])

#2. Given two strings, s1 and s2. Write a program to create
# a new string s3 by appending s2 in the middle of s1.

#Examples:
s1 = 'Aunt'
s2 = 'Sister'
#Result: s3 = SisAuntter
middle = int(len(s2) / 2)
x = s2[:middle:]
x = x + s1
s3 = x + s2[middle:]
print(s3)

#3. Given two strings, s1 and s2, write a program to return
# a new string made of s1 and s2’s first, middle,
# and last characters.

#Example:
s1 = 'America'
s2 = 'Japan'
#Result: s3 = 'AJrpan'
middle1 = int(len(s1)/2)
x1 = s1[middle1]
middle2 = int(len(s2)/2)
x2 = s2[middle2]
s3 = s1[0] + s2[0] + x1 + x2 + s1[-1] + s2[-1]
print(s3)

#4. Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if
# all the characters in the s1 are present in s2.
# The character’s position doesn't matter.

#Example:
s1 = "Yn"
s2 = "PYnative"
#result = True
print("Yn" in s2)

s1 = "Ynf"
s2 = "PYnative"
#result = False
print("Ynf" in s2)

#5. Write a program to split a given string on hyphens
# and display first and last substring.

str1 = 'Emma-is-a-data-scientist'
#result = Emma, scientist
print(str1[0:4] + ', ' + str1[-9:])

#6. Reverse a given string
#Write a program to find the last position of a substring
# “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."
#Result = Last occurrence of Emma starts at index 43
str2 = ''.join(reversed(str1))
print(str2)

index = str1.rfind("Emma")
print(index)


