"""
- strings in python are arrays
- the first position is 0 for array_like objects
"""
hello = "Welcome to python"
# w = 0, e = 1, l = 2
#print(hello[0])
#print(hello[4])
#print(hello[7])
"""
    looping through a string
    for <<variable_name_for_each_character>> in <<string>>:
        statements
"""
for cr in hello:
    print(cr)

"""
    length of a string: len(<<string>>) 
"""
print(len(hello)), # Welcome to python has 17 letters

"""
    check if a character or phrase exists: in > returns True or False
"""
txt = "it's a beautiful day"
print("beau" in txt)
print("day" not in txt)

"""
    slicing of strings: <<string>>[<<start_index>>:<<end_index>>]
    starting position is 0
    slice from a position to end: <<string>>[<<start_index>>:]
    slice from end to a position: use negative index
"""
print(txt[3:7])
print(txt[7:]) #returns the phrase after 0-7 spaces to end
print(txt[-1]) #returns last character in array
print(txt[-4:-1])

"""
lower() or casefold() = returns to lowercase
casefold() use when doing comparison
count() = how many times is the letter in phrase
"""
print(txt.capitalize()) # returns the 1st character as capital letter
print(txt.upper()) # returns everything in capital letter
print(txt.lower()) # returns to lowercase letters
print(txt.count('t')) # returns the number of times a character occurs
print(txt.endswith('x')) # returns true if string ends with a specified value
print(txt.find('ful'))