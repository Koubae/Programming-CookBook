import sqlite3
import csv

conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS book_s')
c.execute('''CREATE TABLE "book_s"(
		"title" TEXT,
		"price" TEXT,
		"rating" TEXT,
		"in_stock" INTEGER)
''')


fname = 'filename.csv'


with open(fname, 'r+') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:
		print(row)
		title = row[0]
		price = row[1]
		rating = row[2]
		in_stock = int(row[3])

		c. execute('''INSERT INTO book_s(title, price, rating, in_stock)
			VALUES (?,?,?,?)''', (title, price, rating, in_stock))

		conn.commit()

#########################################################
#########################################################

import sqlite3
import csv


conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS book_s')
c.execute('''CREATE TABLE "book_s"(
"title" TEXT,
"price" TEXT,
"rating" TEXT,
"in_stock" INTEGER
)
''')

fname = 'book_scrape_new.csv'
new_csv = []
with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

for row in csv_reader:
    title = row[0]
    price = row[1]
    rating = row[2]
    in_stock = row[3]

    c.execute('''INSERT INTO book_s(title, price, rating, in_stock)
    VALUES (?,?,?,?)''', (title, price, rating, in_stock))

    conn.commit()
    conn.close()


def delete_one(id):

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE from database_file_name WHERE rowid = (?)', id)

    conn.commit()
    conn.close()



def lookup(thing):
    
    conn = _sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * from database_file_name WHERE thing=(?)', (thing,))
    item = c.fetchall()
    
    conn.commit()
    conn.close()
    
    return item[0][1]