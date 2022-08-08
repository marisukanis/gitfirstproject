# int, float, complex

"""
integers:
    - whole number without decimal points
    - + or -
    - unlimited length
Floats:
    - numbers with decimal points
    - + or -
    - scientific number 'e' can be used ti denote the power of 10
Complex:
    - complex numbers are written with the imaginary part 'j'

Type conversion/casting:
    - converting from a data type to another
    - str(), int(), float(), complex()
    - you cannot convert from complex to another numeric data type
"""

age = 10
print(type(age))
bal = -989999.80
print(type(bal))
e = 125E6
print(type(e))
comp = 3j+8
print(type(comp))

bal = int(bal)
print(type(bal))



