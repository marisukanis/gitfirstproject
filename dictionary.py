"""
key:value pair
Dictionaries are:
    - ordered
    - changeable
    - do not allow duplicates

<<dict_name>> = {
<<key>>: <<value>>,
<<key>>: <<value>>
}

Json objects are dictionary objects,
a lot of objects are built on dictionary object.
"""
std = {
    'name': 'Maris',
    'age': 32,
    'occupation': 'Data specialist'
}

"""
Access items in a dict:
    - using keys as index:  
        - if you use a key that doesn't exist, it returns an error
    - use get method
        - <<dict_name>>.get(<<key_to_get>>)
        - returns None if key doesn't exist
"""
print(std['age'])
#print(std['ages']) #gets an error "None"
print(std.get('ages'))

"""
Get all keys method:
    - keys method returns a list of all the keys in a dict
    <<dict>>.keys()
"""
print(std.keys())

"""
Add items to a dict:
    - use key_value pair
        <<dict>>[<<ney_key>>] = <<value>>
    - update() - update method
        <<dict>>.update({
                        <<key>>:<<value>>   
                        })
"""
std['is_student'] = 'No'
std['name'] = 'Maris'
print(std)

#stds = {
 #   'names': [],
  #  'ages': {   #this way the key can obtain multiple values

   # }
#}

std.update(
    {
        'best_color': 'black'
    }
)
print(std)

new_dict = {
    'height': 160,
    'weight': 65,
    'hair_color': 'brunette'
}
std.update(new_dict)
print(std)

"""
Remove items in a dictionary:
 - pop(): generates an error if key doesn't exist
 <<dict>>.pop(<<key>>)
 - popitem(): removes the last item in the dict
 - clear(): empties your dict, but the name will still exist
"""
std.pop('height') # removes height from the keys
std.popitem()
print(std)

"""
Loop through a dict: 
.values8): returns the values in the dict
"""
for item in std: # returns the key or use <<dict>>.keys()
    print(item, std[item])

for val in std.values(): # returns dict values
    print(val)

for key, val in std.items(): # returns keys and values
    print(f'{key}: {val}')

print(std.items()) # returns a list of tuples
print(type(std.items()))

# dictionary comprehension
print({k: v for k, v in std.items()}) # returns new dict
print({v: k for k, v in std.items()}) # switches around keys and values
print({k: str(v).upper() for k, v in std.items()}) # changes values to uppercase letters

"""
Nested dictionary:
    <<<dict>> = {
    <<key>>: {
                <<key>>:<<value>>
                ....
                <<key>>:<<value>>
             },
    <<key>>: {
....
}   
"""
students = {
    'Maris': {
        'is_std': False,
        'age': 33
    },
    'Thomas':
        {
            'is_std': True,
            'age': 20
        },
    'Frank': {
        'is_std': True,
        'age': 30,
        'hair_color': 'red'
    }
}
print(students.keys())
print(students)