import operator



class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def do_something(self, c):
        print(self.a, self.b, c)

obj = MyClass()

obj.do_something(100)
operator.methodcaller('do_something', 100)(obj)




class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def do_something(self, *, c):
        print(self.a, self.b, c)

obj.do_something(c=100)

operator.methodcaller('do_something', c=100)(obj)