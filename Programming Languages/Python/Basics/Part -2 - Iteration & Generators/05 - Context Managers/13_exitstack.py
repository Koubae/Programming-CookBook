from contextlib import ExitStack




f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open_file(f_name))
            for f_name in f_names]



f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open_file(f_name))
            for f_name in f_names]
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open(f_name))
            for f_name in f_names]
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)