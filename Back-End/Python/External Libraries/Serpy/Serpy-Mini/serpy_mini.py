import types
import operator


class Field:
    getter_flag = False

    def __init__(self, attr=None, call=False, label=None, required=True):
        self.attr = attr
        self.call = call
        self.label = label
        self.required = required

    def to_value(self, value):
        return value
    to_value.original = True

    def to_value_overridden(self):
        """Check if the Field has been overridden if not a Method it should be overridden
        for instance if is not <class 'method'> but is a <class 'type'> when Field is StrField instance.
        purposely then return False by checking to_value.original flag
        """
        to_value = self.to_value
        if not isinstance(to_value, types.MethodType):
            return True
        return not getattr(to_value, 'original', False)

    def as_getter(self, serializer_field_name, serializer_cls):
        return None


class MethodField(Field):
    """Field for Class' Methods"""
    getter_flag = True

    def __init__(self, method=None, **kwargs):
        super().__init__(**kwargs)
        self.method = method

    def as_getter(self, serializer_field_name, serializer_cls):
        method_name = self.method
        if method_name is None:
            method_name = f'get_{serializer_field_name}'
        return getattr(serializer_cls, method_name)


class StrField(Field):
    to_value = staticmethod(str)


class IntField(Field):
    to_value = staticmethod(int)


class FloatField(Field):
    to_value = staticmethod(float)


class BoolField(Field):
    to_value = staticmethod(bool)


class SerializerBase(Field):
    _field_map = {}


class SerializerMeta(type):
    def __new__(cls, name, bases, attrs):
        direct_fields = {}

        for attr_name, field in attrs.items():
            if isinstance(field, Field):
                direct_fields[attr_name] = field
        for k in direct_fields.keys():
            del attrs[k]

        new_cls = super(SerializerMeta, cls).__new__(cls, name, bases, attrs)

        field_map = cls._get_fields(direct_fields, new_cls)
        fields = cls._compile_fields(field_map, new_cls)

        new_cls._field_map = field_map
        new_cls._compiled_fields = tuple(fields)
        return new_cls

    @staticmethod
    def _get_fields(direct_fields, serializer_cls):
        field_map = {}
        for cls in serializer_cls.__mro__[::-1]:
            if issubclass(cls, SerializerBase):
                field_map.update(cls._field_map)
        field_map.update(direct_fields)
        return field_map

    @staticmethod
    def _compile_fields(field_map, serializer_cls):
        return [SerializerMeta.field_compiler(field, name, serializer_cls)
                for name, field in field_map.items()]

    @classmethod
    def field_compiler(cls, field, name, serializer_cls):
        getter = field.as_getter(name, serializer_cls)
        if getter is None:
            getter = serializer_cls.default_getter(field.attr or name)
        to_value = None
        if field.to_value_overridden():
            to_value = field.to_value
        name = field.label or name
        return name, getter, to_value, field.call, field.required, field.getter_flag


class Serializer(SerializerBase, metaclass=SerializerMeta):
    default_getter = operator.attrgetter

    def __init__(self, instance=None, many=False, data=None, **kwargs):
        if data is not None:
            raise RuntimeError('Input validation not supported')
        super().__init__(**kwargs)
        self.instance = instance
        self.many = many
        self._data = None # Cached the Serialezed Data.

    @property
    def data(self):

        if self._data is None:
            self._data = self.injects(self.instance)
        return self._data

    def injects(self, instance):
        fields = self._compiled_fields # Attr from Metaclass SerializerMeta
        if self.many:
            serialize = self._serialize
            return [serialize(o, fields) for o in instance]
        else:
            return self._serialize(instance, fields)

    def _serialize(self, instance, fields):

        serialized_values = {} # Actual values get stored here
        for (name, getter, to_value, call, required, getter_flag) in fields: # Unpacking tuple self._compiled_fields Attr
            if getter_flag:  # getter_flag from MethodField
                converted = getter(self, instance)
            else:
                try:
                    converted = getter(instance)
                except (KeyError, AttributeError):
                    if required:
                        raise
                    else:
                        continue
                if required or converted is not None:
                    if call:
                        converted = converted()
                    if to_value:
                        converted = to_value(converted)
            serialized_values[name] = converted

        return serialized_values