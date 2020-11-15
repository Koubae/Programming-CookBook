from bank_account import TimeZone, BankAccount, User
import unittest
from datetime import datetime, timezone


class TestTimeZone(unittest.TestCase):

    def test_timezone_incode(self):
        self.assertIn('GMT', TimeZone.CENTRAL_EUROPEAN_STD_TIME)
        self.assertIn('CET', TimeZone.CENTRAL_EUROPEAN_STD_TIME)
        self.assertNotIn('CEST', TimeZone.CENTRAL_EUROPEAN_STD_TIME)

    def test_time(self):
        t = TimeZone('CET')
        t2 = TimeZone('GMT')
        self.assertIsInstance(t, TimeZone, 'T is not instance of TimeZone')
        self.assertTrue(t.pref_time)
        self.assertIsInstance(t.pref_time, list)
        self.assertTrue(datetime.strptime(t.tz_time, '%c'))
        pars_time = datetime.strptime(t.tz_time, '%c')
        self.assertIsInstance(pars_time, datetime)
        self.assertTrue(t.tz_region == str(timezone.utc))
        self.assertTrue(datetime.strptime(t.time_utc, '%Y%m%dT%H%M%S'))
        self.assertFalse(t == t2); self.assertTrue(t != t2)
        print(datetime.strftime(t.get_tx(), '%Y%m%dT%H%M%S'))
        self.assertTrue(datetime.strftime(t.get_tx(), '%Y%m%dT%H%M%S'))
        print(datetime.strftime(t.current_dt_utc(), '%Y%m%dT%H%M%S'))
        self.assertTrue(datetime.strftime(t.current_dt_utc(), '%Y%m%dT%H%M%S'))


class TestUser(unittest.TestCase): ...


if __name__ == '__main__':
    unittest.main()