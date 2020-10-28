from collections import namedtuple
from datetime import datetime


file = 'tickets.csv'

# TODO Improve Function Efficiency
# Converts Item in each row to Python Data.


class CSVGenerator:
    def __init__(self, file_csv):
        self.file = file_csv
        self._header = next(self.gen_header(file))

    def __repr__(self):
        return f'CSVGenerator(file={self.file}, header={self._header})'

    def __iter__(self):
        return self.inject_data(file)

    # Generate Header of the File.
    def gen_header(self, file_):
        def get_header():
            with open(file_, 'r') as f:
                top = f.readline()
                header = top.split(',')
                header = ['_'.join(column.split()).lower()
                          for column in header]
                CardParkTicket = namedtuple('CarParkTicket', header)
                return CardParkTicket
        yield get_header()

    @staticmethod
    def convert_data(data_list):
        converted_list = list()
        for item in data_list:
            try:
                value = datetime.strptime(item, '%d/%m/%Y')  # Converts Data into Datetime Object
                converted_list.append(value)
            except ValueError:
                try:
                    value = int(item)
                    converted_list.append(value)
                except ValueError:
                    value = str(item)
                    converted_list.append(value)
        return converted_list

    @staticmethod
    def extract_data(file_):
        with open(file_, 'r') as f:
            for line in f:
                yield line.split('\n')[:-1]  # Read file and Split all items

    def inject_data(self, file_):
        row = self.extract_data(file)
        header = self._header
        next(row)
        while True:
            try:
                get_str = ''.join(next(row))
                my_row = get_str.split(',')  # Make it back to List
                my_row = self.convert_data(my_row)
                try:
                    data = header(*my_row)
                    yield data
                except TypeError:  # Catch if row has more than 9 items
                    if len(my_row) > 9:
                        for item in range(len(my_row) - 9):  # iterates over the difference of len
                            remove_item = my_row.pop()  # removes last item
                            my_row[-1] += remove_item  # attach it to the last one
                            data = header(*my_row)
                            yield data
            except StopIteration:
                break

  # Get vehivle_make per violation_description
    def get_violation(self):
        brand = dict()
        for row in self:
            if brand.get(row.vehicle_make):
                brand[row.vehicle_make] += bool(row.violation_description)
            else:
                brand.__setitem__(row.vehicle_make, int(bool(row.violation_description)))
        return brand

    def max_violation(self):
        brand = self.get_violation()
        max_val = [None, 0]
        for i in brand:
            if max_val[1] < brand[i]:
                max_val[1] = brand[i]
                max_val[0] = i
        result = {max_val[0] : max_val[1]}
        return result






my_reader = CSVGenerator(file)

print(my_reader.max_violation())