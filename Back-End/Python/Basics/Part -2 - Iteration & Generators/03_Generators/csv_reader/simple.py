from collections import namedtuple
from datetime import datetime


file = 'tickets.csv'
# 10/5/2016

def conver_data(data_list):
    converted_list = list()
    for i in data_list:
        try:
            x = datetime.strptime(i, '%d/%m/%Y')
            converted_list.append(x)
        except ValueError:
            try:
                x = int(i)
                converted_list.append(x)
            except ValueError:
                x = str(i)
                converted_list.append(x)
    return converted_list




# date = datetime.strptime(date, '%d/%m/%Y') # Converts Data into Datetime Object


def gen_header(file):
    def gen_h():
        with open(file, 'r') as f:
            header = f.readline()
            header = header.split(',')
            header = ['_'.join(column.split()).lower() for column in header]
            CarParkTicket = namedtuple('CarParkTicket', header)
            return CarParkTicket

    yield gen_h()


def extract_data(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.split('\n')[:-1]  # Read file and Split all items


# noinspection PyArgumentList
def inject_data(file):
    row = extract_data(file)
    header = next(gen_header(file))  # Calls Header Generator
    next(row) # Skips the Header
    while True:
        try:
            get_str = ''.join(next(row)) # Make it to Str
            my_row = get_str.split(',') # Make it back to List
            my_row = conver_data(my_row)
            try:
                data = header(*my_row)
                yield data
            except TypeError: # Catch if row has more than 9 items
                if len(my_row) > 9:
                    for item in range(len(my_row) - 9): # iterates over the difference of len
                        remove_item = my_row.pop() # removes last item
                        my_row[-1] += remove_item # attach it to the last one
                        data = header(*my_row)
                        yield data
        except StopIteration:
            break


x = extract_data(file)
#print(list(x))
y = inject_data(file)
for i in list(y):
    for x in i:
        if type(x) == str:
            print(x)


###############################################################
###############################################################
###############################################################

def gen_header(file):
    def gen_h():
        with open(file, 'r') as f:
            header = f.readline()
            header = header.split(',')
            header = ['_'.join(column.split()).lower() for column in header]
            CarParkTicket = namedtuple('CarParkTicket', header)
            return CarParkTicket

    yield gen_h()


def extract_data(file):
    with open(file, 'r') as f:
        for _ in f:
            yield f.read().split('\n')[:-1]  # Read file and Split all items


def inject_data(file):
    extraced_data = next(extract_data(file))
    for row in list(extraced_data):
        row = row.split(',')
        header = next(gen_header(file))
        try:
            header = header(*row)
            yield header
        except TypeError: # Catch if row has more than 9 items
            if len(row) > 9:
                for item in range(len(row) - 9): # iterates over the difference of len
                    remove_item = row.pop() # removes last item
                    row[-1] += remove_item # attach it to the last one
                    header = header(*row)
                    yield header