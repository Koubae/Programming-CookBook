import json
import re
from pprint import pprint
from decimal import Decimal

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            # we have at least one `Point'
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        # recursive function to find and replace points
        # received object could be a dictionary, a list, or a simple type
        if isinstance(obj, dict):
            # first see if this dictionary is a point itself
            if '_type' in obj and obj['_type'] == 'point':
                # could have used: if obj.get('_type', None) == 'point'
                obj = Point(obj['x'], obj['y'])
            else:
                # root object is not a point
                # but it could contain a sub-object which itself
                # is or contains a Point object
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj

j = '''
{
    "a": 100,
    "b": 0.5,
    "rectangle": {
        "corners": {
            "b_left": {"_type": "point", "x": -1, "y": -1},
            "b_right": {"_type": "point", "x": 1, "y": -1},
            "t_left": {"_type": "point", "x": -1, "y": 1},
            "t_right": {"_type": "point", "x": 1, "y": 1}
        },
        "rotate": {"_type" : "point", "x": 0, "y": 0},
        "interior_pts": [
            {"_type": "point", "x": 0, "y": 0},
            {"_type": "point", "x": 0.5, "y": 0.5}
        ]
    }
}
'''
print(json.loads(j))
{'a': 100, 'b': 0.5, 'rectangle': {'corners': {'b_left': {'_type': 'point', 'x': -1, 'y': -1}, 'b_right': {'_type': 'point', 'x': 1, 'y': -1}, 't_left': {'_type': 'point', 'x': -1, 'y': 1}, 't_right': {'_type': 'point', 'x': 1, 'y': 1}}, 'rotate': {'_type': 'point', 'x': 0, 'y': 0}, 'interior_pts': [{'_type': 'point', 'x': 0, 'y': 0}, {'_type': 'point', 'x': 0.5, 'y': 0.5}]}}
pprint(json.loads(j))
print('==='*15)
pprint(json.loads(j, cls=CustomDecoder))

# {'a': 100,
#  'b': 0.5,
#  'rectangle': {'corners': {'b_left': Point(x=-1, y=-1),
#                            'b_right': Point(x=1, y=-1),
#                            't_left': Point(x=-1, y=1),
#                            't_right': Point(x=1, y=1)},
#                'interior_pts': [Point(x=0, y=0), Point(x=0.5, y=0.5)],
#                'rotate': Point(x=0, y=0)}}

CustomDecoder = json.JSONDecoder(parse_float=Decimal)
d = CustomDecoder.decode(j)
pprint(d)
# {'a': 100,
#  'b': Decimal('0.5'),
#  'rectangle': {'corners': {'b_left': {'_type': 'point', 'x': -1, 'y': -1},
#                            'b_right': {'_type': 'point', 'x': 1, 'y': -1},
#                            't_left': {'_type': 'point', 'x': -1, 'y': 1},
#                            't_right': {'_type': 'point', 'x': 1, 'y': 1}},
#                'interior_pts': [{'_type': 'point', 'x': 0, 'y': 0},
#                                 {'_type': 'point',
#                                  'x': Decimal('0.5'),
#                                  'y': Decimal('0.5')}],
#                'rotate': {'_type': 'point', 'x': 0, 'y': 0}}}


class CustomDecoder(json.JSONDecoder):
    base_decoder = json.JSONDecoder(parse_float=Decimal)

    def decode(self, arg):
        obj = self.base_decoder.decode(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            # we have at least one `Point'
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        # recursive function to find and replace points
        # received object could be a dictionary, a list, or a simple type
        if isinstance(obj, dict):
            # first see if this dictionary is a point itself
            if '_type' in obj and obj['_type'] == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                # root object is not a point
                # but it could contain a sub-object which itself
                # is or contains a Point object nested at some level
                # maybe another dictionary, or a list
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            # received a list - need to run each item through make_pts
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj

print(json.loads(j, cls=CustomDecoder))
# {'a': 100,
#  'b': Decimal('0.5'),
#  'rectangle': {'corners': {'b_left': Point(x=-1, y=-1),
#    'b_right': Point(x=1, y=-1),
#    't_left': Point(x=-1, y=1),
#    't_right': Point(x=1, y=1)},
#   'rotate': Point(x=0, y=0),
#   'interior_pts': [Point(x=0, y=0), Point(x=0.5, y=0.5)]}}
result = json.loads(j, cls=CustomDecoder)
pt = result['rectangle']['interior_pts'][1]
print(type(pt.x), type(pt.y))
# <class 'decimal.Decimal'> <class 'decimal.Decimal'>