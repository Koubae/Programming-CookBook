class IntegerValue:
    def __init__(self, name):
        self.storage_name = '_' + name 
        
    def __set__(self, instance, value):
        setattr(instance, self.storage_name, int(value))
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return getattr(instance, self._storage_name, None)
        
class Point2D:
    x = IntegerValue('x')
    y = IntegerValue('y')


p1 = Point2D()
p2 = Point2D()

p1.x = 10.1
p1.y = 20.2
print(p1.__dict__)
# {'_x': 10, '_y': 20}
p2.x = 100.1
p2.y = 200.2
print(p2.__dict__)
# {'_x': 100, '_y': 200}

# So this approach can work just fine, but there are a few drawbacks:

# The user needs to specify the name of the property twice
# We assume that _ + name is not also used by the class in which the descriptor exists (so that could be a major problem)
# We assume we can add an attribute to the instance - but what if it uses slots?
# One way we could get around each of those problems is by using the descriptor instance itself to store the instance values. But as we saw earlier, we can't just set an attribute in the descriptor instance, since that would be shared across multiple instances of the class containing the descriptor.

# Instead, we are going to assume that the instance is a hashable object, and use a dictionary in the descriptor to store instance specific values:


class IntegerValue:
    def __init__(self):
        self.values = {}
        
    def __set__(self, instance, value):
        self.values[instance] = int(value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)

class Point2D:
    x = IntegerValue()
    y = IntegerValue()


p1 = Point2D()
p2 = Point2D()

p1.x = 10.1
p1.y = 20.2