"""
While loop:
    - executes a set of sentence until the condition is no longer valid
"""
i = 10
while i > 0:
    print(i)
    i -= 1      # i = i -1

"""
break:
- stops the loop even if the condition is valid
"""
i = 10
#while i > 3:
 #   print(i)
  #  if i == 6:
   #     break
    #i -= 2

#for x in range(i):
 #   print(x)
  #  if x == 6:
   #     break

"""
continue:
- stops the current iteration and advances to the next
"""
for x in range(i):
    if x == 6:
        continue
    print(x)

# range(start, end, step)
# range (10) - start
# range (-1) - end
# range (-1) - step

name = input('What is your name')
# input allows you to type in the answer from terminal
print(f'My name is {name}')
