from urllib.parse import urljoin, urlparse, quote
import os
import builtins.decode
# x = ('Hello', )
# x = list('Hello')
# z = 2
# x = {'hi':2}
# # y = x.copy()
# # print(y)

# url_ = urlparse('https://realpython.com/python3-object-oriented-programming/')
# print(url_.netloc)


# class ClassA(object):

#     def display(self):
#         print("Class A")

# class ClassB(object):
#     __class__ = ClassA

#     def display(self):
#         print("Class B")

# instance = ClassB()

# print(type(instance))
# print(instance.__class__)
# instance.display()


# def is_file_allowed(filename):

#     allowed_extensions = 'png'
#     return ('.' in filename and filename.rsplit('.', 1)[1].lower() in           
#             map(lambda x: x.lower(), allowed_extensions))
# allowed_extensions = ['png', 'jpg']
# x = is_file_allowed('mario.png')
# y = 'mario.png'
# print(y.rsplit('.', 1)[1] in map(lambda  x: x.lower(), allowed_extensions))
# print(list(map(lambda x: x.lower(), allowed_extensions)))

x = os.urandom(24)
y = 'hi'

if isinstance(x, bytes):
    print(x)
if isinstance(y, str):
    print('y')

print(type(x))
# x.encode('utf-8')

# print(x.decode('utf-8'))
print('ciao'.encode('utf-8'))
print(type(x))
x = x.strip()
print(type(x))
x = str(x)
print(type(x))
print(help(decode))