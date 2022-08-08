"""
Tuples:
- ordered
- unchangeable
- created/denoted with ()
- allow duplicates
"""

tuple1 = ('oranges',) # put comma after a tuple with 1 item; tuple item
print(type(tuple1))
tuple2 = ('oranges') # string item
print(type(tuple2))

"""
Add items: convert tuple to a list, append the item and convert back to a tuple
"""

x = list(tuple1) # create a list as tuple
x.append('lemon') # add a lemon to the list
tuple1 = tuple(x) # convert from list to tuple
print(tuple1)

tuple2 = ('star fruit',)
tuple1 += tuple2
print(tuple1)

"""
Unpacking of tuple

The number of items in your tuple should be equal to the length of the tuple
if not, you use '*' to unpack the remaining to a list
"""
fruit1, fruit2, fruit3 = tuple1
print(fruit2)

fruit, *fruit_2 = tuple1
print(fruit_2)
