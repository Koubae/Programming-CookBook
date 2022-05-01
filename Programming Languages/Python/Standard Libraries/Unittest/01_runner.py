import unittest
# Import packages

class Test(unittest.TestCase):
    print('All set!')


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)


if __name__ == '__main__':
    run_tests(Test)