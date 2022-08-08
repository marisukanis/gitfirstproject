"""
Set:
    - a collection
    - unordered - when you print the same set, it comes in different order
    - unchangeable
    - unidentified, you cannot access them through index
    - created/denoted with {}
    - sets do not allow duplicates (you can't have items with the same value)
"""

myset = {'mangoes', 'guavas', 'berries', 'honeydew', 'mangoes'} # last duplicated mango does not appear in the printed list
print(myset)
print(len(myset))

for x in myset:
    print(x)

print('honeydew' in myset) # returns true/false

"""
Add items to a set:
- add <<set>>.add(<<item>>)
- update - adds items from a set into another set
    <<set1>>.update(<<set2>>)
- add any iterable/collection to a set
"""

myset.add('cantaloupe') # adds cantaloupe to the set
print(myset)

nuts = {'cashew', 'peanut', 'almonds', 'guavas'} # new set
myset.update(nuts) # adds "nuts" set to "myset"
print(myset)

citrus = {'oranges', 'tangerine', 'lemon', 'lime'}
myset.update(citrus)
print(myset)

"""
Removing elements from a set:
    - remove <<set>>.remove(<<item>>) this generates an error if the item doesn't exist
    - pop: removes the last item in the set, but remember that a set is unordered, 
        thus you have no idea/control over what is being removed
    - discard: doesn't return error if item isn't found
    - clear
"""
myset.remove('guavas')
print(myset)
#myset.remove('passion fruit') # does not work, gets an error, because it doesn't exist in the set
myset.discard('passion fruit') # does not return error
myset.pop() # have no control of what is being removed, because set is unordered
print(myset)

"""
Joining of set:
- union: create a new set with item from the 2 sets, removes duplicates
"""
set1 = {'peanut', 'oranges', 'berries', 'almonds', 'cantaloupe'}
set2 = {'cantaloupe', 'mangoes', 'honeydew', 'lime', 'tangerine', 'lemon'}
set3 = {'oranges', 'almonds', 'berries', 'peanut', 'mangoes'}

set3 = set1.union(set2)
print(set3)

"""
To get common values(duplicates) within a set:
    - intersection: <<set1>>.intersection(<<set2>>)
    - intersection_update = what is common to both
"""
set1.intersection(set2) # returns all values from set1 and also duplicate one from set2
print(set1)
set1.intersection_update(set2) # returns common values from both sets
print(set1)

print(set3)
print(set2)
set3.symmetric_difference_update(set2) # returns what is different in set2 and set3
print(set3)

print(set3.isdisjoint(set2)) # returns true if 2 sets have no common ground/are not overlapping
