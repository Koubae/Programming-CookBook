#  Note taken from --> https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369 & https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/11158224#11158224
import os, sys, inspect, warnings
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import time
import datetime
import uuid


class BaseFilter(object):

    def __init__(self, name, options=None, data_type=None, key_name=None):
        self.name = name
        self.options = options
        self.data_type = data_type
        self.key_name = key_name
    
    def get_options(self, view):

        options = self.options
        if options:
            if callable(options):
                options = options()
            return options
        return None
    
    def validate(self, value):

        try:
            self.clean(value)
            return True
        except ValueError:
            return False
    
    def clean(self, value):
        return value
    
    def apply(self, query, value):
        raise NotImplementedError()
    
    def operation(self):
        raise NotImplementedError()

    def __unicode__(self):
        return self.name

class BaseBooleanFilter(BaseFilter):

    def __init__(self, name, options=None, data_type=None):
        super(BaseBooleanFilter, self).__init__(name,
                                                ('1', 'Yes'),
                                                ('0', 'No'),
                                                data_type)
    def validate(self, value):
        return value in ('0', '1')


class BaseIntFilter(BaseFilter):

    def clean(self, value):
        return int(value)


class BaseFloatFilter(BaseFilter):

    def clean(self, value):
        return float(value)


class BaseIntListFilter(BaseFilter):

    def clean(self, value):
        return [int(v.strip()) for v in value.split(',') if v.strip()]


class BaseFloatListFilter(BaseFilter):

    def clean(self, value):
        return [float(v.strip()) for v in value.split(',') if v.strip()]


class BaseDateFilter(BaseFilter):

    def __init__(self, name, options=None, data_type=None):
        super(BaseDateFilter, self).__init__(name, 
                                            options,
                                            data_type='datepicker')
    def clean(self, value):
        return datetime.datetime.strptime(value, '%Y-%m-%d').date()


class BaseDateBetweenFilter(BaseFilter):

    def clean(self, value):
        return [datetime.datetime.strptime(rande, '%Y-%m-%d').date()
                for range in value.split(' to ')]
    
    def operation(self):
        return 'between'
    
    def validate(self, value):

        try:
            value = [datatime.datetime.strptime(range, '%Y-%m-%d').date()
                    for range in value.split(' to ')]
            if (len(value) == 2) and (value[0] <= value[1]):
                return True
            else:
                return False
        except ValueError:
            return False


class BaseDateTimeFilter(BaseFilter):

    def __init__(self, name, options=None, data_type=None):
        super(BaseDateTimeFilter, self).__init__(name,
                                                options,
                                                data_type='datetimepicker')
    
    def clean(self, value):
        return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')


class BaseDateTimeBetweenFilter(BaseFilter):

    def clean(self, value):
        return [datetime.datetime.strptime(range, '%Y-%m-%d %H:%M:%S')
                for range in value.split(' to ')]

    def operation(self):
        return 'between'
    
    def validate(self, value):

        try:
            value = [datetime.datetime.strptime(range, '%Y-%m-%d %H:%M:%S')
                    for range in value.split(' to ')]
            if (len(value) == 2) and (value[0] <= value[1]):
                return True
            else:
                return False
        except ValueError:
            return False


class BaseTimeFilter(BaseFilter):

    def __init__(self, name, options=None, data_type=None):
        super(BaseTimeFilter, self).__init__(name,
                                            options,
                                            data_type='timepicker')
    
    def clean(self, value):
        timetuple = time.strptime(value, '%H:%M:%S')
        return datetime.time(timetuple.tm_hour,
                            timetuple.tm_min,
                            timetuple.tm_sec)


class BaseTimeBetweenFilter(BaseFilter):

    def clean(self, value):
        timetuples = [time.strptime(range, '%H:%M:%S')
                    for range in value.split(' to ')]
        return [
            datetime.time(timetuple.tm_hour, timetuple.tm_min, timetuple.tm_sec)
            for timetuple in timetuples
        ]
    
    def operation(self):
        return 'between'
    
    def validate(self, value):

        try:
            timetuples = [time.strptime(range, '%H:%M:%S')
                        for range in value.split(' to ')]
            if (len(timetuples) == 2) and (timetuples[0] <= timetuples[1]):
                return True
            else:
                return False
        except ValueError:
            raise
            return False


class BaseUuidFilter(BaseFilter):

    def __init__(self, name, options=None, data_type=None):
        super(BaseUuidFilter, self).__init__(name, options, data_type='uuid')
    
    def clean(self, value):
        value = uuid.UUID(value)
        return str(value)


class BaseUuidListFilter(BaseFilter):

    def clean(self, value):
        return [str(uuid.UUID(v.strip())) for v in value.split(',') if v.strip()]
    
    def convert(*args):

        def _inner(func):
            func._converter_for = list(map(lambda x: x.lower(), args))
            return func
        return _inner()


class BaseFilterConverter(object):

    def __init__(self):
        self.converters = dict()

        for p in dir(self):
            attr = getattr(self, p)

            if hasattr(attr, '_converter_for'):
                for p in attr._converter_for:
                    self.converters[p] = attr
                    