from contextlib import contextmanager


@contextmanager
def open_file(f_name):
    print(f'opening file {f_name}')
    f = open(f_name)
    try:
        yield f
    finally:
        print(f'closing file {f_name}')
        f.close()


f_names = 'file1.txt', 'file2.txt', 'file3.txt'

enters = []
exits = []
for f_name in f_names:
    ctx = open_file(f_name)
    enters.append(ctx.__enter__)
    exits.append(ctx.__exit__)

files = [enter() for enter in enters]

# opening file file1.txt
# opening file file2.txt
# opening file file3.txt

while True:
    try:
        rows = [next(f).strip('\n') for f in files]
    except StopIteration:
        break
    else:
        row = ','.join(rows)
        print(row)

# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3

for fn in exits[::-1]:
    fn(None, None, None)


# closing file file3.txt
# closing file file2.txt
# closing file file1.txt



f_names = 'file1.txt', 'file2.txt', 'file3.txt'

exits = []
files = []
try:
    for f_name in f_names:
        ctx = open_file(f_name)
        files.append(ctx.__enter__())
        exits.append(ctx.__exit__)

    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)
finally:
    for fn in exits[::-1]:
        fn(None, None, None)


# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt


class NestedContexts:
    def __init__(self, *contexts):
        self._enters = []
        self._exits = []
        self._values = []

        for ctx in contexts:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)

    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())
        return self._values

    def __exit__(self, exc_type, exc_value, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_value, exc_tb)
        return False

with NestedContexts(open_file('file1.txt'),
                   open_file('file2.txt'),
                   open_file('file3.txt')) as files:
    print('do work here')


with NestedContexts(open_file('file1.txt'),
                   open_file('file2.txt'),
                   open_file('file3.txt')) as files:
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)



# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt


file_names = 'file1.txt', 'file2.txt', 'file3.txt'
contexts = [open_file(f_name) for f_name in f_names]
with NestedContexts(*contexts) as files:
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)


class NestedContexts:
    def __init__(self):
        self._exits = []

    def __enter__(self):
        return self

    def enter_context(self, ctx):
        self._exits.append(ctx.__exit__)
        value = ctx.__enter__()
        return value

    def __exit__(self, exc_type, exc_value, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_value, exc_tb)
        return False

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with NestedContexts() as stack:
    files = [stack.enter_context(open_file(f_name)) for f_name in f_names]

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with NestedContexts() as stack:
    files = [stack.enter_context(open_file(f_name)) for f_name in f_names]

    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

