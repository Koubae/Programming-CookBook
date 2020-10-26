from collections import namedtuple


def cast(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)


def cast_row(data_types, data_row):
    return [cast(data_type, value)
            for data_type, value in zip(data_types, data_row)]


cars = []

with open('cars.csv') as file:
    row_index = 0
    for line in file:
        if row_index == 0:
            headers = line.strip('\n').split(';')
            Car = namedtuple('Car', headers)
        elif row_index == 1:
            data_types = line.strip('\n').split(';')

        else:
            data = line.strip('\n').split(';')
            data = cast_row(data_types, data)
            car = Car(*data)
        
            cars.append(car)
        row_index += 1

print(cars[0])



