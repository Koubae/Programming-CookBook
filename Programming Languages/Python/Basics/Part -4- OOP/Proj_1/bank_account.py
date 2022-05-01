from random import randint
from datetime import datetime, timezone, timedelta
from collections import namedtuple
from functools import wraps


class TimeZone:
    CENTRAL_EUROPEAN_STD_TIME = {
        'GMT': [0, 'Greenwich Mean Time', 'GMT'],
        'CET': [1, 'Central European Time', 'CET']
    }
    time_zone = timezone.utc  # class variable to store the timezone - default to UTC

    def __init__(self, pref_time):
        self._pref_time = self.CENTRAL_EUROPEAN_STD_TIME[pref_time]
        self.tz_time = self.pref_time[0], self.pref_time[-1]
        self.tz_region = self.get_tx().tzname()
        self.tz_time = self.get_tx().ctime()
        self.time_utc = self.current_dt_utc().strftime('%Y%m%dT%H%M%S')

    @property
    def pref_time(self):
        """Get the Preferred time Zone as list [offset, time zone name, time zone code] """
        return self._pref_time

    @staticmethod
    def current_dt_utc():
        "Get non-naive UTC current Time"
        return datetime.now(timezone.utc)

    def set_tz(self, offset, tz_code):
        """
        Gets the Time zone Off set
        :param offset: hours offset from CENTRAL_EUROPEAN_STD_TIME Variable
        :param tz_code: Timezone code  from CENTRAL_EUROPEAN_STD_TIME Variable
        :return: <class 'datetime.timezone'>
        """
        self.time_zone = (timezone(timedelta(hours=offset), tz_code))
        return self.time_zone

    def get_tx(self):
        ":return <class 'datetime.datetime'> based on the Time Zone"
        current = self.current_dt_utc()
        return current.astimezone(self.time_zone)


class BankAccount:
    TRANSACTION_CODE = ('D', 'W', 'I', 'X')
    INTEREST = 0.5
    confirmation_number = namedtuple('confirmation_number', '''
                transaction_code
                transaction_id
                account_number                
                time_utc
                time
                value''')
    TRANSACTION_LOOKUP = dict()
    TRANSACTION_COUNTER = 0
    BANK_LOOKUP = set() # Faster Lookup by confirmation number

    def __init__(self, account_number):
        self._account_number = account_number

    @property
    def account_number(self):
        self._account_number = [str(randint(0, 9)) for num in range(6)]
        return ''.join(self._account_number)

    @classmethod
    def declined(cls, balance, value):
          try:
              raise ValueError(f'''Operations Aborted, insufficient founds to perform the operation.
You have {balance} but transaction required {value}.
                '''.strip('\t'))
          except ValueError as err:
              print(err)

    @classmethod
    def check_transaction(cls, balance, value):
        if (balance + value) >= 0:
            return balance + value
        else:
            cls.declined(balance, value)
            return 'Declined'

    @classmethod
    def commit_transaction(cls, transaction):
        get_code = cls.transaction_map(transaction)
        with open('log.txt', 'a') as f:
            f.writelines(get_code + ', ' + str(transaction) + '\n') # Writes Transaction_code in a log
        return get_code

    @classmethod
    def transaction_map(cls, transaction):
        transaction_code = '-'.join([str(value) for value in transaction[:-2]])
        cls.TRANSACTION_LOOKUP[transaction.transaction_id] = transaction_code # Save a Mapping of transaction
        cls.BANK_LOOKUP.add(transaction_code)
        return transaction_code

    def bank_lookup(self): ...


class User(BankAccount):

    USER_TRANSACTIONS = dict()
    USER_LOOKUP = set() # Faster Lookup by confirmation number

    def __init__(self, first_name: str, last_name: str, balance: int, user_time):
        super().__init__(account_number=super().account_number)
        self.first_name = first_name
        self.last_name = last_name
        try:
            self.user_time = TimeZone(user_time.upper())
        except KeyError as err:
            print('===' * 15)
            print(f'Incorrect time preference {err}')
            self.user_time = TimeZone('GMT') # If KeyError, Systems sets default time to Greenwich Mean Time
            print('---'*15)
            print(f'Setting Default time to {self.user_time.pref_time[1], self.user_time.tz_region}')
            print('===' * 15)
        if balance >= 0:
            self._balance = balance
        else:
            try:
                ValueError(self.declined(0, value=balance))
            except ValueError as err:
                print(err)

    @property
    def balance(self):
        return getattr(self, '_balance')

    @balance.getter
    def balance(self):
        return getattr(self, '_balance')

    @balance.setter
    def balance(self, value: float):
        new_balance = self._balance + value
        if value < 0:
            return self.declined(self._balance, value)
        setattr(self, '_balance', value)
        print(f'Your new Balance is: {self.balance:.2f}')
        return self.balance

    def generate_confirmation_num(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            if fn.__name__[0].upper() in super().TRANSACTION_CODE:
                self.TRANSACTION_COUNTER += 1
                get_tt = fn.__name__[0].upper() # Get the transaction Type
                get_ti = self.TRANSACTION_COUNTER # Get the transaction ID
                _new_transaction = super().confirmation_number(get_tt, get_ti, self._account_number,
                                                               self.user_time.time_utc,
                                                               self.user_time.tz_time, args)

                commit_ = super().commit_transaction(_new_transaction)
                self.USER_TRANSACTIONS[commit_] = _new_transaction
                self.USER_LOOKUP.add(commit_)
            return fn(self, *args, **kwargs)
        return wrapper

    @generate_confirmation_num
    def deposit(self, value):
        self.balance += value
        return self.balance

    @generate_confirmation_num
    def withdrawal(self, value):
        transaction = self.check_transaction(self.balance, value)
        if transaction != 'Declined':
            self.balance -= value
        else:
            return transaction

    @generate_confirmation_num
    def interest_deposit(self):
        calc_interest = (self.balance//100)*super().INTEREST
        self.balance += calc_interest
        return self.balance

    def check_user_transactions(self):
        "Check all User transaction, not taking care of transaction time"
        for tr in self.USER_LOOKUP:
            print(tr)

    def get_transaction(self):
        for tr in self.USER_LOOKUP:
            break
        return tr

    def user_lookup_(self, transaction):
        if transaction in self.USER_LOOKUP:
            return self.USER_TRANSACTIONS[transaction]





#
a = User('Fede', 'b', 100, 'CET')
# # b = User('B', 'BA', 1)
# # c = User('C', 'CA', 1)
# # print(a.first_name, a.account_number)
# # print(b.first_name, b.account_number)
# # print(c.first_name, c.account_number)
# t = TimeZone('CET')
# # print(t.pref_time)
# # print(t.current_dt_utc())
# # print(timezone(timedelta(hours=1), 'GMT'))
# x = t.current_dt_utc()
# a.deposit(10)
# a.deposit(10)
#
# value = a.get_transaction()
# result = a.user_lookup_(value)
# print(result.transaction_code)
# print(result.transaction_id)
# print(result.account_number)
# print(datetime.strptime(result.time_utc, '%Y%m%dT%H%M%S'))
# print(result.time)
# print(result.value)
a.deposit(1j)
