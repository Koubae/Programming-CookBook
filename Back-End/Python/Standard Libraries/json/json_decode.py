import json



# ----------------------#
# ---> object_hook <--- #
#-----------------------#

json_datetime = '''

    {
        "value": "2018-10-21T09:14:15"
    }
'''

def obj_hook(arg):
    for i in arg.keys():
        try:
            arg[i] = datetime.strptime(arg[i], '%Y-%m-%dT%H:%M:%S')
        except ValueError as err:
            print(err)
            try:
                arg[i] = datetime.fromisoformat(arg[i])
            except ValueError as err:
                print(err)
                arg[i] = str(arg[i])
        return arg

print(json.loads(date_, object_hook=obj_hook))


# -------------------------#
# ---> obj_pairs_hoos <--- #
#--------------------------#
def obj_pairs_hook(arg):
    return arg

weird_json = '{"x": 1, "x": 2, "x": 3}'
print(json.loads(weird_json, object_pairs_hook=obj_pairs_hook))