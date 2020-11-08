from datetime import date, datetime
from decimal import Decimal
from functools import singledispatch
import json


class Stock:
    def __init__(self, symbol: str, date: date, open_: Decimal,
                 high: Decimal, low: Decimal, close: Decimal, volume: int):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return f'{self.__class__.__name__}({self.tojson()})'

    def tojson(self):
        return vars(self)


class Trade:
    def __init__(self, symbol: str, timestamp: date, order: str, price: Decimal, volume: int, commission: Decimal):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def __repr__(self):
        return f'{self.__class__.__name__}({self.tojson()})'

    def tojson(self):
        return vars(self)


activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22),
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22),
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22),
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],

    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}


@singledispatch
def formatter(arg):
    try:
        return arg.tojson()
    except (TypeError, AttributeError):
        return str(arg)


@formatter.register(date)
def _(arg):
    return arg.strftime('%Y-%m-%dT%H:%M:%S')


@formatter.register(Decimal)
def _(arg):
    return f'Decimal({str(arg)})'


x = json.dumps(activity, default=formatter, indent=2)
y = json.loads(x)
print(x)