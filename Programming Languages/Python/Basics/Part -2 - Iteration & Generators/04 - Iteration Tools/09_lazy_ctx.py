def read_data():
    with open('nyc_parking_tickets_extract.csv') as f:
        return list(csv.reader(f, delimiter=',', quotechar='"'))

for row in read_data():
    print(row)