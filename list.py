"""
LIST EXERCISE
"""
"""
1. Reverse a given list in python
"""
info = ['karl', '100', 'Red', 'Mangoes']
list.reverse(info)
print(info)

"""
2. Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item from both the list, 
then the 1st index item, and so on till the last element. 
any leftover items will get added at the end of the new list.
Hint: use list comprehension with zip function
"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
#result = ['My', 'name', 'is', 'Kelly']
print(list3)

"""
3. Write a Python program to find the second largest number in the given list.
"""
list1 = [10, 20, 4]
#result: 10

list2 = [70, 11, 20, 4, 100]
#result: 70

list1.sort()
list2.sort()
print(list1[-2], list2[-2])

"""
4. Concatenate two list
Hint: use list comprehension
<<new_list>> = [expression for item in list1 for y in list2]
"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [x + y for x in list1 for y in list2]
print(list3)
#result = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

"""
5. Write a program to find value 20 in the list, and if it is present, 
replace it with 200. Only update the first occurrence of an item.
"""
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

"""
6. Count number of occurrences of x in the given list
"""
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
#result : 3  #10 appears three times in given list.
print(lst.count(x))

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 16
#result : 0
print(lst.count(x))

"""
7. Write a program to remove all occurrences of item 20
Hint: list comprehension
"""
list1 = [5, 20, 15, 20, 25, 50, 20]
val = 20
list1 = [i for i in list1 if i !=val]
print(list1)

"""
8. Write a program to return the middle value of a list. 
If there are 2 middle values, return the second
"""
names = ['Ade', 'orange', 'pineapple', 'apples', 'mangoes']
#result = 'pineapple'
middle = names[len(names)//2]
print(middle)

age = [10, 3, 45, 67, 89.0, 45]
#result = 67
second_middle = age[len(age)//2]
print(second_middle)