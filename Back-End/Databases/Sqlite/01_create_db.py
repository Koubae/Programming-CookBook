import sqlite3

conn = sqlite3.connect('tax_vat.db')

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS country_vat')
c.execute("""CREATE TABLE country_vat(
          country text,
          vat_rate real,
          threshold real)""")

conn.commit()

conn.close()