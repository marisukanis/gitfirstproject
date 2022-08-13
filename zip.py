"""
Zip:
 - easily combine 2 lists
 - in order to see the content of a zip, it must be casted to a list
 - if different lengths, the result will be the shortest list
"""
name = ['Maris', 'Thomas', 'Frank', 'Inna', 'Corey']
surname = ['Ukanis', 'Mei', 'White', 'Mcneil']
age = [28, 30, 20, 18]

zip(name, surname, age)
print(list(zip(name, surname, age)))
