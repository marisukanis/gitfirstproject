"""
File Operations:
    - creating a file
    - reading a file
    - updating a file
    - deleting a file

Open method is fundamental function, which takes 2 arguments:
open(<<filename>>, <<mode>>)

Four basics modes:
r = read       #default, opens the file for reading, error if file does not exist
w = write      #opens the file for writing at the beginning, creates the file if not exist
a = append     #opens the file for appending, if file not exist, creates the file
x = create     #creates the new file, error if file exist

Two additional modes:
t = text mode   #default
b = binary
"""
# # to read a file
# f = open('test.txt')
# print(type(f))
# lines = 1
# while lines < 10:
#     print(f.readline())
#
#
# f = open('test.txt')
# while True:
#     print(f.readline())
#     if not f.readline():
#         break
import os

f = open('test.txt', 'w')
f.write('Ohh, it is going to rain. \n The beautiful day isnt for outdoor activites')
f.close()

with open('test.txt', 'a') as f:
    f.write('I wont be able to cycle. \n I think I will paint')

if os.path.exists('test.txt'):
    os.remove('test.txt')   #removes a file