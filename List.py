"""
    lists are used to store multiple values in a variable
    lists are denoted/created using [] brackets
    lists are ordered collection of items
    allow duplicates
    changeable - add, remove, replace
"""
import string

mylist = ['apples','mangoes', 2, 7.5, 'red']
print(type(mylist)) # returns the type of the list
print(mylist[0]) # returns the first item on the list
print(mylist[-1]) # returns the last item on the list
print(mylist[2:4])
print(mylist[2:])

# use in to check if a value exists in a list
print('guava' in mylist) #checks if ypu have guava in list and returns as true/false

"""
Add items to a list
- append: adds to the end of the list
- insert: adds at a specific index
    <<list>>.insert(<<position>>, value)
- extend: appends elements from a list to another list, appends at the end
    <<current_list>>.extend(<<new_append_list>>)
"""

mylist.append('guavas') #adds guavas to the end of the list
mylist.append('grapes') #adds grapes to the end of the list
mylist.insert(2, 'blueberries') #adds to the list on the 2nd position
mylist.insert(0, 'mangoes') #adds to the list on the 1st position
print(mylist) # prints the list

exotic_fruits = ['cashew', 'wild blueberries', 'passion fruit']

mylist.extend(exotic_fruits)
print(mylist)

mylist[4] = "corn" # replace items on the lists
print(mylist)

"""
Remove items in a list:
    - remove: <<list>>.remove(<<item>>)
        - with duplicate instance, the first is removed
    - pop: removes the last item <<list>>.pop()
        <<list>>.pop(<<index>>): removes item at the position
    - clear: removes all the items in a list
"""
mylist.remove(7.5) # removes items on the list, only one argument at a time
mylist.pop()
mylist.remove('apples')
print(mylist)
mylist.pop(1)
print(mylist)
exotic_fruits.clear() #deletes the content in the list
print(exotic_fruits)

age = [12, 14, 25, 39, 67, 45, 13]
print(min(age))
print(max(age))
print(sum(age))
print(sum(age) / len(age))

mylist.sort()
age.sort() # sorts the age numbers in order
print(mylist)
print(age)

mylist.reverse() # reverses your list, last item becomes 1st, 1st item the last
print(mylist)

""""
Looping through a list
- for loop
    for <<variable>> in <<list>>:
        statements
- range: allows you to loop through the index
- list comprehension
"""

ages = 10
name = "Maris"
print(ages)

print(f"My name is {name}, I am {ages} years old")
print("My name is " + name + "I am " + str(ages) + "years old ")
print("my name is {} and I am {} years old".format(name, ages))

for var in mylist:
    print(f"I love {var}") # add f in string
    print("I love "+ var)
    print("I love {}".format(var))

for item in age:
    print(item/2)

"""
range(start, stop, step)
default step is 1
"""
range(10) # 0 to 9
range(5, 10) # 5 to 9, if you want the other way round, use minus

for i in range(len(age)):
    print(f"index{i}: {age[i]}")

"""
List Comprehension:
    - creates a new list
    - short method of creating a list from an existing list
    - filter and perform operations
    
    [expression for <<variable_name>> in <<list>> <<optional: condition>>]
"""
x = [print(f"My age is {x}") for x in age]

new_age = [x for x in age if x%2 == 0] # returns only even numbers of age
print(new_age)
new_age = [x + 10 for x in age if x%2 == 0] # adds +10 to even numbers
print(new_age)

upp_list = [var.upper() for var in mylist] # returns each item in the list as upper case
print(upp_list)


