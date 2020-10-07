import string
import time

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)


def membership_test(n, container):

    for i in range(n):
        if 'p' in container:
            pass

start = time.perf_counter()
membership_test(10_000_000, char_list)
end = time.perf_counter()
print('list membership: ', end-start)

start = time.perf_counter()
membership_test(10_000_000, char_tuple)
end = time.perf_counter()
print('tuple membership: ', end-start)

start = time.perf_counter()
membership_test(10_000_000, char_set)
end = time.perf_counter()
print('set membership: ', end-start)

# OUTPUT
# list membership:  2.5244251999999996
# tuple membership:  2.5487871
# set membership:  0.34697259999999996
