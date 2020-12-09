from main import download_manager
import unittest


class Test(unittest.TestCase):

    def test_one_keyword(self):
        main_keyword = ['neutral']
        download_manager(main_keyword, extra_keywords=None, total=2)

    def test_download_false(self):
        main_keyword = ['neutral']
        download_manager(main_keyword, extra_keywords=None, total=2, download=False)

    def test_custom_dir(self):
        main_keywords = ['pizza', 'pasta']
        extra_k = ['pomodoro', 'salami', 'tuna']
        my_dir = './my_dir/'
        download_manager(main_keywords, extra_keywords=extra_k, download_dir=my_dir, total=2)


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)


if __name__ == '__main__':
    run_tests(Test)