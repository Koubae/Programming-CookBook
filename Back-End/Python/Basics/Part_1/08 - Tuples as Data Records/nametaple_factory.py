from collections import namedtuple


def defaulted_namedtuple(class_name, **fields):
    Struct = namedtuple(class_name, fields.keys())
    Struct.__new__.__defaults__ = tuple(fields.value())
    return Struct


Vector2D = defaulted_namedtuple('Vector2D', 
        x1= None, y1=None,
        x2=None, y2=None,
        origin_x=0, origin_y=0)

Vector2D._fields 

v1 = Vector2D(10, 10, 20, 20)
