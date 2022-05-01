from collections import namedtuple

Point2D = namedtuple('Point2D', ('x', 'y'))
Point3D = namedtuple('Point3D', 'x y z')
pt1 = Point2D(10, 20)

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

StockExt = namedtuple('StockExt',
                      '''symbol year month day open high low 
                      close previous_close''')


print(Stock._fields)
# ('symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close')
new_fields = Stock._fields + ('previous_close',)

# Create a New NT
StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))
print(StockExt._fields)

# Variant
' '.join(Stock._fields) + ' previous_close'
StockExt = namedtuple('StockExt',
                      ' '.join(Stock._fields) + ' previous_close')

djia_ext = StockExt(*djia, 25_000)
print(djia_ext)

# _make method
djia_ext = StockExt._make(djia + (25_000, ))
print(djia_ext)

#StockExt(symbol='DJIA', year=2018, month=1,
# day=25, open=26313, high=26458, low=26260,
# close=26393, previous_close=25000)