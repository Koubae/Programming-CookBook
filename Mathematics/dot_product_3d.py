class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False


pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)

pt3d_1
pt3d_1 == pt3d_2


# How about calculating the dot product of two points (considering them as vectors starting at the origin)?
# The formula would be: a.b = a.x b.x + a.y + b.y + a.z b.z
# For the 3D point we would need to do the following:

def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z + b.z

dot_product_3d(pt3d_1, pt3d_2)

# But for our 2D point, is a tuple as well, we can write a generic function that would work equally well with a 3D named tuple too:

def dot_product(a, b):
    return sum(e[0] * e[1] for e in  zip(a, b))


a = Point2D(1, 2)
b = Point2D(10, 20)
print(a)
print(b)
print(tuple(a))
print(tuple(b))
print(list(zip(a, b)))

u = (1, 2, 3)
v = (10, 20, 30)
list(zip(u, v))

print([e[0] * e[1] for e in zip(a, b)])
print(sum([e[0] * e[1] for e in zip(a, b)]))
print(dot_product(a, b))

pt4d_1 = (1, 1, 1, 10)
pt4d_2 = (2, 2, 2, 10)

print(dot_product(pt4d_1, pt4d_2))