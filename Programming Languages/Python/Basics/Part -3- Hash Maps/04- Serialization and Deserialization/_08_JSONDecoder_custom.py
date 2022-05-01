import json


j = '''
    {
        "a": 100,
        "b": [1, 2, 3],
        "c": "python",
        "d": {
            "e": 4,
            "f": 5.5
        }
    }
'''


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        print("decode:", type(arg), arg)
        return "a simple string object"


print(json.loads(j, cls=CustomDecoder))

# decode: <class 'str'>
#     {
#         "a": 100,
#         "b": [1, 2, 3],
#         "c": "python",
#         "d": {
#             "e": 4,
#             "f": 5.5
#         }
#     }
#
# a simple string object


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

j_points = '''
{
    "points": [
        [10, 20],
        [-1, -2],
        [0.5, 0.5]
    ]
}
'''

j_other = '''
{
    "a": 1,
    "b": 2
}
'''

class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        if 'points' in arg:
            obj = json.loads(arg)
            return "parsing object for points"
        else:
            return super().decode(arg)

print(json.loads(j_points, cls=CustomDecoder))
json.loads(j_other, cls=CustomDecoder)


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        if 'points' in obj:  # top level
            obj['points'] = [Point(x, y)
                             for x, y in obj['points']]
        return obj

print(json.loads(j_points, cls=CustomDecoder))
# {'points': [Point(x=10, y=20), Point(x=-1, y=-2), Point(x=0.5, y=0.5)]}
print(json.loads(j_other, cls=CustomDecoder))
#{'a': 1, 'b': 2}



