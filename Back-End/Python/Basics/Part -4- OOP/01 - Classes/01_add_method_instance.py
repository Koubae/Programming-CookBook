
from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name
        
    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))
        
    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)
        # if attribute exists we'll get it back, otherwise it will be None
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('You must first register a do_work method')


math_teacher = Person('Eric')
english_teacher = Person('John')

def work_math(self):
    return f'{self.name} will teach differentials today.'


def work_english(self):
    return f'{self.name} will analyze Hamlet today.'

math_teacher.register_do_work(work_math)
print(math_teacher.__dict__)


english_teacher.register_do_work(work_english)
english_teacher.do_work()
print(english_teacher.__dict__)