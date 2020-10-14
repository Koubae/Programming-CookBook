import sys

numbers = [int(a) for a in sys.argv[1:]]

print(sum(numbers))

# and call it as follows:
# python example3.py 1 2 3 4 5 6


import sys

for i in range(1, len(sys.argv), 2):
    print(sys.argv[i], sys.argv[i+1])