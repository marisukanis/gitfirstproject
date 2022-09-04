# from operator import add, sub
#
# d = {
#     'add': add,
#     'sub': sub
# }
#
# print(d.get('mul', add)(5, 4))
#
# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def get(self):
#         pass
#
# class B(A):
#     def set(self):
#         return '8'
#
# b = B()
# print(b.set())

# x = 0
#
# while True:
#     print(f'Value of x = {x}')
#     if not x > 0:
#         break
#     x -= 1
#
# print(x)
#
# def

def decorator(func):
    def wrapper(*args, **kwargs):
        print('Wraps the func function..')
        val = func(*args, **kwargs)
        return val
    return wrapper(func)

@decorator
def add(a, b):
    return a + b

print(add(1,2))