from datetime import date, datetime
from decimal import Decimal
from functools import singledispatch
import json
from pprint import pprint


class Stock:
    def __init__(self, symbol: str, date: date, open: Decimal,
                 high: Decimal, low: Decimal, close: Decimal, volume: int):
        self.symbol = symbol
        self.date = date
        self.open = open
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



class FormatterEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(skipkeys=True,
                         allow_nan=False,
                         indent=' ',
                         separators=(',', ' : ')
                         )
    @singledispatch
    def default(self, arg):

        if isinstance(arg, Stock) or isinstance(arg, Trade):
            return vars(arg)
        elif isinstance(arg, date):
            return arg.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(arg, Decimal):
            return f'Decimal({str(arg)})'
        elif isinstance(arg, int):
            print('Int >>>', arg)
        else:
            return super().default(arg)


z = json.dumps(activity, cls=FormatterEncoder)


class CustomDecoder(json.JSONDecoder):
    # def __ini__(self, dicts):
    #     super().__init__()
    #     self.dict = []
    def decode(self, arg):
        activity = {}
        obj = json.loads(arg)
        extract_data = [obj[i] for i in obj]

        for i in range(len(extract_data)):
            check_data = extract_data[i]

            for item in check_data:
                check_inside = item

                for k, v in check_inside.items():
                    try:
                        check_inside[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
                    except (ValueError, TypeError) as err:
                        try:
                            check_inside[k] = eval(v)
                        except (NameError, TypeError, SyntaxError) as err:
                            pass

                try:
                    activity[item['symbol']] = (Stock(**check_inside))
                except TypeError:

                    activity[item['symbol']] = (Trade(**check_inside))

        return activity




# print('==='*15)
y = json.loads(z, cls=CustomDecoder)
# for i in y.items():
#     pprint(i)

