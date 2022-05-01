from numbers import Real
from collections import UserDict

class IntDict:
    def __init__(self):
        self._d = {}

    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a real number.')
        self._d[key] = value

    def __getitem__(self, key):
        return int(self._d[key])

d = IntDict()
d['a'] = 10.5


class IntDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a real number.')
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))

d = IntDict()
d['a'] = 10.5


class IntDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a real number.')
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return int(super().__getitem__(key))



d = IntDict()

d['a'] = 10.5
d['b'] = 100.5


class LimitedDict(UserDict):
    def __init__(self, keyset, min_value, max_value, *args, **kwargs):
        self._keyset = keyset
        self._min_value = min_value
        self._max_value = max_value
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key not in self._keyset:
            raise KeyError('Invalid key name.')
        if not isinstance(value, int):
            raise ValueError('Value must be an integer type.')
        if value < self._min_value or value > self._max_value:
            raise ValueError(f'Value must be between {self._min_value} and {self._max_value}')
        super().__setitem__(key, value)

d = LimitedDict({'red', 'green', 'blue'}, 0, 255, red=10, green=10, blue=10)
print(d)
# {'red': 10, 'green': 10, 'blue': 10}
d['red'] = 200
print(d)

d['purple'] = 100


# ---------------------------------------------------------------------------
# KeyError