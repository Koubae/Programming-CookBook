from collections import namedtuple, defaultdict
from datetime import datetime
from functools import partial

file_name = 'tickets.csv'

with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')

column_names = [header.replace(' ', '_').lower()
                for header in column_headers] # Gets Columns names

Ticket = namedtuple('Ticket', column_names) # Create a Named Tuple based on column named


def read_data(): # Reads all data as Generator Function
    with open(file_name) as f:
        next(f)
        yield from f


# Parsing data
def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_string(value, *, default=None):
    try:
        cleaned = str(value).strip()
        if not cleaned: # => Checks is string is empty, if it is then ignores the Row
            return default
        else:
            return cleaned
    except ValueError:
        return default


column_parser = (parse_int,
                 parse_string,
                 partial(parse_string, default=''),
                 partial(parse_string, default=''),
                 parse_date,
                 parse_int,
                 partial(parse_string, default=''),
                 parse_string,
                 lambda x: parse_string(x, default='')
                 )  # => Demostrates lambda insted of partial


def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    parsed_data = [func(field)
                   for func, field in
                   zip(column_parser, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default


def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed

def violation_counts_by_make():
    makes_counts = defaultdict(int)
    for data in parsed_data():
        makes_counts[data.vehicle_make] += 1
    return {make: cnt
            for make, cnt in
            sorted(makes_counts.items(), key=lambda t: t[1], reverse=True)
            }


####################
##TESTING##########
####################

raw_data = read_data()
for _ in range(5):
    print(next(raw_data))



print(parse_date('31/31/2000', default='N/A'))

for row in read_data():
    parsed_row = parse_row(row)
    if parsed_row is None:
        print(list(zip(column_names, row.strip('\n').split(','))), end='\n\n')

parsed_rows = parsed_data()
for _ in range(5):
    print(next(parsed_rows))

print(violation_counts_by_make())