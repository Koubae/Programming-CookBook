import operator


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('Test Method running....')


obj = MyClass()

f = operator.attrgetter('a')
f(obj)
# 10

my_var = 'b'
operator.attrgetter(my_var)(obj)
# 20
f = operator.attrgetter('a', 'b', 'c')
f(obj)
# (10, 20, 30)

# Attrgetter return a object's method
f = operator.attrgetter('test')
obj_test_method = f(obj)
obj_test_method()
# 
test method running...
operator.attrgetter('a', 'b')(obj)
# 10, 20)

f = lambda x: (x.a, x.b, x.c)
f(obj)
# (10, 20, 30)

f = lambda x: (x[2], x[3])
f([1, 2, 3, 4])
# (3, 4)