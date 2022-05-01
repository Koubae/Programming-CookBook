import sys

sys.stdout.write('Hello World\n')
x = 5
y = 10

temp = sys.stdout
sys.stdout = open('temp.txt', 'a')
for i in range(10):
    print('SPAM' + 'EGGS')
sys.stdout.close()
sys.stdout = temp

sys.stdout = open('log.txt', 'a')
for i in range(100):
    print(x,y)

print(x+y)
with open('log2.txt', 'a') as f:
    for i in range(100):
        print(x * y, file=f)

# you may also be able to use the __stdout__
# attribute in the sys module, which refersto the original value
# sys.stdout had at program startup time. You still need to
# restore sys.stdout tosys.__stdout__ to go back to this original stream value,
# though. See the sys module documentation formore details.

class FileFaker:
    def write(self, string):
        pass# Do something with printed text in string

# Sends to class write method
sys.stdout = FileFaker()
print('something')

myobj = FileFaker()
print('someObject', file=myobj)