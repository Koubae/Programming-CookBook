import sys


class OutToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stdout = sys.stdout

    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stdout = self._file

    def __exit__(self, exc_type, exc_value, exc_tb):
        sys.stdout = self._current_stdout
        if self._file:
            self._file.close()
        return False


with OutToFile('test.txt'):
    print('Line 1')
    print('Line 2')

print('back to console output')
# back to console output


with open('test.txt') as f:
    print(f.readlines())

#
# ['Line 1\n', 'Line 2\n']

