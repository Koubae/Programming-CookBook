import sys

# let's create a dictionary of the name/value pairs

# the parameter names
keys = sys.argv[1::2]
values = sys.argv[2::2]
print(keys)
print(values)

# next create a dictionary so we can easily look up the value for a given key
args = {k: v for k, v in zip(keys, values)}
print(args)

# finally let's assign the arguments to variables:
first_name = args.get('--first-name')
last_name = args.get('--last-name')
print(first_name, last_name)

# call it this way:
# python example5.py --last-name Cleese --first-name John