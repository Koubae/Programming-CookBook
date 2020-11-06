from datetime import datetime
import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            super().default(arg)


custom_encoder = CustomJSONEncoder()
custom_encoder.encode(True)
print(json.dumps(dict(name='test', time=datetime.utcnow()), cls=CustomJSONEncoder))
# {"name": "test", "time": "2020-11-06T03:32:11.017915"}


def custom_encoder(arg):
    print('Custom encoder called...')
    if isinstance(arg, str):
        return f'some string: {arg}'

# -----------#
# skipkeys
# -----------#

d = {10: "int", 10.5: "float", 1+1j: "complex"}
json.dumps(d, skipkeys=True)
# '{"10": "int", "10.5": "float"}'


# -----------#
# indent & separatos
# -----------#
d = {
    'name': 'Python',
    'age': 27,
    'created_by': 'Guido van Rossum',
    'list': [1, 2, 3]
}

print(json.dumps(d, indent='---', separators=('', ' = ')))

# {
# ---"name" = "Python"
# ---"age" = 27
# ---"created_by" = "Guido van Rossum"
# ---"list" = [
# ------1
# ------2
# ------3
# ---]
# }

print(json.dumps(d, separators=(',', ':')))
# {"name":"Python","age":27,"created_by":"Guido van Rossum","list":[1,2,3]}


class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(skipkeys=True,
                         allow_nan=False,
                         indent='---',
                         separators=('', ' = ')
                         )

    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)

d = {
    'time': datetime.utcnow(),
    1+1j: "complex",
    'name': 'Python'
}



print(json.dumps(d, cls=CustomEncoder))
# {
# ---"time" = "2018-12-29T22:27:26.689488"
# ---"name" = "Python"
# }


class CustomEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            obj = dict(
                datatype="datetime",
                iso=arg.isoformat(),
                date=arg.date().isoformat(),
                time=arg.time().isoformat(),
                year=arg.year,
                month=arg.month,
                day=arg.day,
                hour=arg.hour,
                minutes=arg.minute,
                seconds=arg.second
            )
            return obj
        else:
            return super().default(arg)


d = {
    'time': datetime.utcnow(),
    'message': 'Testing...'
}

print(json.dumps(d, cls=CustomEncoder, indent=2))


# {
#   "time": {
#     "datatype": "datetime",
#     "iso": "2018-12-29T22:27:27.668208",
#     "date": "2018-12-29",
#     "time": "22:27:27.668208",
#     "year": 2018,
#     "month": 12,
#     "day": 29,
#     "hour": 22,
#     "minutes": 27,
#     "seconds": 27
#   },
#   "message": "Testing..."
# }