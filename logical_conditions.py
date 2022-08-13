"""
Logical conditions evaluate to boolean = true/false
a == b #equals
a != b #not equals
a < b #greater
etc
"""
if 10 < 5:
    print('less than 5')
else:
    print('not less than 5')

"""
True and True = True
True and False = False
False and True = False
False and False = False
"""
marks = [90, 75, 80, 60, 72]
grade = []
for mark in marks:
    if mark >= 90: # 90 - 100
        grade.append('A+')
    elif mark >= 80 and mark < 90: # 80-89
        grade.append('A')
    elif mark >= 70 and mark < 80: # 70-79
        grade.append('B')
    elif mark >= 60 and mark < 70:  # 60-69
        grade.append('C')
    else:
        grade.append('Fail')

60 >= mark < 70 # another way to show it instead of elif mark >= 60 and mark < 70:  # 60-69
print(grade)

"""
Ternary operators / Conditional expressions
<<value_if_true>> if <<condition>> else <<value_if_false>>
"""
print('no equal') if 10 != 5 else print('equals')


