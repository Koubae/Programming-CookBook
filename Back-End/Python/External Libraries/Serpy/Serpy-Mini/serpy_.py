import types
import operator
import six


class Field(object):
    getter_takes_serializer = False

    def __init__(self, attr=None, call=False, label=None, required=True):
        self.attr = attr
        self.call = call
        self.label = label
        self.required = required

    def to_value(self, value):

        return value
    to_value._serpy_base_implementation = True

    def _is_to_value_overridden(self):
        """Check if the Field has been overridden"""
        to_value = self.to_value
        # If to_value isn't a method, it must have been overridden.
        if not isinstance(to_value, types.MethodType):
            print('HEREEEEEEE', self.__class__, type(to_value))
            return True
        return not getattr(to_value, '_serpy_base_implementation', False)

    def as_getter(self, serializer_field_name, serializer_cls):
        return None




class MethodField(Field):

    getter_takes_serializer = True

    def __init__(self, method=None, **kwargs):
        super(MethodField, self).__init__(**kwargs)
        self.method = method

    def as_getter(self, serializer_field_name, serializer_cls):
        method_name = self.method
        if method_name is None:
            method_name = 'get_{0}'.format(serializer_field_name)
        return getattr(serializer_cls, method_name)


class StrField(Field):
    """A :class:`Field` that converts the value to a string."""
    to_value = staticmethod(six.text_type)


class IntField(Field):
    """A :class:`Field` that converts the value to an integer."""
    to_value = staticmethod(int)


class FloatField(Field):
    """A :class:`Field` that converts the value to a float."""
    to_value = staticmethod(float)


class BoolField(Field):
    """A :class:`Field` that converts the value to a boolean."""
    to_value = staticmethod(bool)


class SerializerBase(Field):
    _field_map = {}




def _compile_field_to_tuple(field, name, serializer_cls):
    getter = field.as_getter(name, serializer_cls)
    if getter is None:
        #If getter is None means that the default Field was used
        getter = serializer_cls.default_getter(field.attr or name)

    # Only set a to_value function if it has been overridden for performance.
    to_value = None
    if field._is_to_value_overridden():
        to_value = field.to_value

    # Set the field name to a supplied label; defaults to the attribute name.
    name = field.label or name

    return (name, getter, to_value, field.call, field.required,
            field.getter_takes_serializer)


class SerializerMeta(type):

    @staticmethod
    def _get_fields(direct_fields, serializer_cls):
        field_map = {}
        # Get all the fields from base classes.
        for cls in serializer_cls.__mro__[::-1]:
            if issubclass(cls, SerializerBase):
                field_map.update(cls._field_map)
        field_map.update(direct_fields)
        return field_map

    @staticmethod
    def _compile_fields(field_map, serializer_cls):

        return [
            _compile_field_to_tuple(field, name, serializer_cls)
            for name, field in field_map.items()
        ]

    def __new__(cls, name, bases, attrs):
        # Fields declared directly on the class.
        direct_fields = {}
        # Take all the Fields from the attributes.
        for attr_name, field in attrs.items():
            # print(attr_name, field)
            if isinstance(field, Field):
                direct_fields[attr_name] = field ## serpy.Field = Added in a separate Dict
        for k in direct_fields.keys():
            del attrs[k] ## Removes from the Attrs the Fields instances

        real_cls = super(SerializerMeta, cls).__new__(cls, name, bases, attrs)

        field_map = cls._get_fields(direct_fields, real_cls) ### [field_map]

        compiled_fields = cls._compile_fields(field_map, real_cls) # -> tuple(name, getter, to_value, field.call, field.required,
                                                                        #field.getter_takes_serializer)
        real_cls._field_map = field_map # Map (Dictionary) with all Serpy.Fieds
        real_cls._compiled_fields = tuple(compiled_fields) # Tuple with Serpy Field and Filed Class Vars() [3]
        return real_cls




class Serializer(six.with_metaclass(SerializerMeta, SerializerBase)):
    #: The default getter used if :meth:`Field.as_getter` returns None.
    default_getter = operator.attrgetter
    def __init__(self, instance=None, many=False, data=None, context=None,
                 **kwargs):
        if data is not None:
            raise RuntimeError(
                'serpy serializers do not support input validation')

        super().__init__(**kwargs)
        self.instance = instance
        self.many = many
        self._data = None
        # print(self._compiled_fields)

    def __repr__(self):
        return f'{vars(self)}'

    def _serialize(self, instance, fields):
        """_serialize is called internally by self.to_value"""
        v = {} ## v is where the Item get actually serialized
        for name, getter, to_value, call, required, pass_self in fields: # Unpacking tuple self._compiled_fields
            if pass_self: # [4] pass_self
                result = getter(self, instance)

            else:

                try: ### Try/Except block | Check if required or not Default required=True
                    result = getter(instance)
                except (KeyError, AttributeError):
                    if required:
                        raise
                    else:
                        continue
                if required or result is not None:
                    if call:
                        result = result()
                    if to_value:
                        result = to_value(result)
            v[name] = result
        return v

    def to_value(self, instance):
        fields = self._compiled_fields
        if self.many:
            serialize = self._serialize
            return [serialize(o, fields) for o in instance]
        return self._serialize(instance, fields)

    @property
    def data(self):
        # [2] data
        # Cache the data for next time .data is called.
        if self._data is None:
            self._data = self.to_value(self.instance)
        return self._data


### [field_map]  Injects serpy.Fields + original class to _get_fields, checks whether the subclass is
# SerializerBase's subclass

## [2] data calls the self.tovalue

## [3] self._compiled_fields called in __new__  SerializerMeta Metaclass is a tupple with all the fields, in
# indx [0] there is the filds name (as Original class has named, can be the 'labeled one) in [1] there is operator.attrgetter
# instance (uses the original name, in case of label= was used


# [4] pass_self is the value of Class instance attribute  getter_takes_serializer, it is True only if
# Field is MethodField