import itertools
import numbers
from datetime import timedelta, datetime
from collections import namedtuple


Confirmation = namedtuple('Confirmation', 'account_number, transaction_code, transaction_id, time_utc, time')


class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')

        self._name = str(name).strip()
        # technically we should check that offset is a
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minutes offset must be an integer.')

        if offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')

        # for time delta sign of minutes will be set to sign of hours
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        # offsets are technically bounded between -12:00 and 14:00
        # see: https://en.wikipedia.org/wiki/List_of_UTC_time_offsets
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)

    def __repr__(self):
        return (f"TimeZone(name='{self.name}'."
                f"offset_hours={self._offset_hours},"
                f"offset_minutes={self._offset_minutes}")


class Account:
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5

    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interes': 'I',
        'rejected': 'X'
    }

    def __init__(self, account_number, firt_name, last_name, timezone=None, initial_balance=0):
        self._account_number = account_number
        self.first_name = firt_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone('UTC', 12, 0)
        self.timezone = timezone
        self._balance = Account.validate_real_number(initial_balance, min_value=0) # Static Method

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First Name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last Name')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def timezone(self):
        return self._timezone

    @property
    def balance(self):
        return self._balance

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time Zone must be a valid TimeZone object.')
        self._timezone = value

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest must be a real number.')
        if value < 0:
            raise ValueError('Interest rate cannot be a negative.')
        cls._interest_rate = value

    def validate_and_set_name(self, property_name: str, value: str, field_title: str):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, property_name, value)

    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')
        if min_value is not None and value < min_value:
            raise ValueError(f'Value must be at least {min_value}')
        return value

    def generate_confirmation_code(self, transaction_code):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'''{transaction_code}-{self._account_number}-
                   {dt_str}-{next(Account.transaction_counter)}'''

    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            raise ValueError('Invalid confirmation code!!!')

        transaction_code, account_number, raw_dt_utc, transaction_id = parts

        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError as ex:
            raise ValueError('Invalid transaction datetime') from ex

        if preferred_time_zone is None:
            preferred_time_zone = TimeZone('UTC', 0, 0)
        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Invalid TimeZone Specified')

        dt_preffered = dt_utc + preferred_time_zone.offset
        dt_preffered_str = f'''{dt_preffered.strftime('%Y-%m-%d %H:%M:%S')}
                               ({preferred_time_zone.name})'''
        return Confirmation(account_number, transaction_code,
                            transaction_id, dt_utc.isoformat(), dt_preffered_str)

    def deposit(self, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Deposit value must be a real number.')
        if value <= 0:
            raise ValueError('Deposist value must ba a positive number.')

        transaction_code = Account._transaction_codes['deposit'] # Class Property
        conf_code = self.generate_confirmation_code(transaction_code)
        self._balance += value
        return conf_code

    def withdraw(self, value):
        accepted = False
        if self.balance - value < 0:
            transaction_code = Account._transaction_codes['rejected']
        else:
            transaction_code = Account._transaction_codes['withdraw']
            accepted = True

        conf_code = self.generate_confirmation_code(transaction_code)
        if accepted:
            self._balance -= value
        return conf_code

    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(self._transaction_codes['interest'])
        self._balance += interest
        return conf_code


a = Account('A100', 'Eric', 'Idle', initial_balance=100)

# try:
#     a.deposit(-100)
# except ValueError as ex:
#     print(ex)
#
# try:
#     a.withdraw("100")
# except ValueError as ex:
#     print(ex)
