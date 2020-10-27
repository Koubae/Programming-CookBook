import functools

class cached_property(object):
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


class LogHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    @cached_property
    def load_log_file(self):
        with open(self.file_path) as f:
            # the file is to big that I have to cost 2s to read all file
            return f.read()

log_handler = LogHandler('./sys.log')
# only the first time call will cost 2s.
print(log_handler.load_log_file)
# return value is cached to the log_handler obj.
print(log_handler.load_log_file)