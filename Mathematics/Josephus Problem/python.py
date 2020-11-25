import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result

class Test3(unittest.TestCase):

    ALL_SURVIVOR = [(7, 3), (11, 9), (1, 300), (14, 2), (100, 1)]
    RESULTS = [4, 5, 1, 13, 100]

    def test_reminder(self):

        def lastSurvivor(n, k):
            circle = list(range(1, n+1))
            k -= 1 # Set Step to Array index equivalent
            idx = k # Pointer to Step, used for calc the reminder Algorithm
            while len(circle) > 1:
                dead = circle.pop(idx)
                idx = (idx+k) % len(circle) # Re set the index in comparrison with the Array length

            return circle

        results = [lastSurvivor(*survivor) for survivor in self.ALL_SURVIVOR]
        for survivor in results:
            print(f'Using Reminder Algo, Survivor= ', survivor[0])
            # Using Reminder Algo, Survivor=  4
            # Using Reminder Algo, Survivor=  5
            # Using Reminder Algo, Survivor=  1
            # Using Reminder Algo, Survivor=  13
            # Using Reminder Algo, Survivor=  100
        for idx, result in enumerate(self.RESULTS):
            self.assertTrue([idx], result)

    def test_deque(self):
        from collections import deque

        def lastSurvivor(n, k):
            circle = deque(list((range(1, n+1))))
            while len(circle) > 1:
                circle.rotate(-k) # Move list k steps to left so that n[0] is the Dead person
                circle.pop()
            return circle

        results = [lastSurvivor(*survivor) for survivor in self.ALL_SURVIVOR]
        for survivor in results:
            print(f'Using Reminder Deque, Survivor= ', survivor[0])
            # Using Reminder Deque, Survivor=  4
            # Using Reminder Deque, Survivor=  5
            # Using Reminder Deque, Survivor=  1
            # Using Reminder Deque, Survivor=  13
            # Using Reminder Deque, Survivor=  100
        for idx, result in enumerate(self.RESULTS):
            self.assertTrue([idx], result)


    def test_recursive(self):

        def lastSurvivor(n, k):
            if n == 1:
                return 1
            else:
                return (lastSurvivor(n-1, k) + k-1) % n+1


        results = [lastSurvivor(*survivor) for survivor in self.ALL_SURVIVOR]
        for survivor in results:
            print(f'Using Reminder Recursive, Survivor= ', survivor)
            # Using Reminder Recursive, Survivor=  4
            # Using Reminder Recursive, Survivor=  5
            # Using Reminder Recursive, Survivor=  1
            # Using Reminder Recursive, Survivor=  13
            # Using Reminder Recursive, Survivor=  100
        for idx, result in enumerate(self.RESULTS):
            self.assertTrue([idx], result)



if __name__ == '__main__':
    run_tests(Test3)