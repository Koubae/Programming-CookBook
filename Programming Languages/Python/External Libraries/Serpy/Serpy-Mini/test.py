import unittest
import serpy_ as serpy
import serpy_mini as serpym


class Obj(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Test(unittest.TestCase):

    class Foo(object):
        y = 1
        z = 2
        super_long_thing = 10
        old_label = 'LABEL'

        def x(self):
            return 5

    class FooSerializer(serpy.Serializer):
        w = serpy.Field(attr='super_long_thing')
        x = serpy.Field(call=True)  # Function in Foo
        plus = serpy.MethodField()

        old_label = serpy.Field(label='New_Label')
        not_required = serpy.Field(required=False)
        not_serpy = 'I AM NOT A INSTANCE OF FIELD!!'

        def get_plus(self, obj):
            return obj.y + obj.z

        def __repr__(self):
            return f'{vars(self)}'

    class MySerializer(serpym.Serializer):
        w = serpym.Field(attr='super_long_thing')
        x = serpym.Field(call=True)  # Function in Foo
        plus = serpym.MethodField()

        old_label = serpym.Field(label='New_Label')
        not_required = serpym.Field(required=False)
        not_serpy = 'I AM NOT A INSTANCE OF FIELD!!'

        def get_plus(self, obj):
            return obj.y + obj.z

        def __repr__(self):
            return f'{vars(self)}'


    def test_a(self):
        f = self.Foo()
        # serializer = serpy.Serializer
        inst_foo = self.FooSerializer()
        serialized = self.FooSerializer(f, label='My Serializer')
        serialized.data

    def test_mini_serpy(self):
        mini_serpy = serpym.Serializer
        real_serpy = serpy.Serializer
        self.assertNotEqual(mini_serpy, real_serpy)
        equal_ = []
        not_equal = []
        m_serpy_l = [c for c in mini_serpy.__mro__]
        # [<class 'serpy_mini.Serializer'>, < class 'serpy_mini.SerializerBase' >, < class 'serpy_mini.Field' >, < class 'object' >]
        real_serpy_l = [c2 for c2 in real_serpy.__mro__]
        # [<class 'serpy_.Serializer' >, < class 'serpy_.SerializerBase' >, < class 'serpy_.Field' >, < class 'object' >]
        for c in mini_serpy.__mro__:
            for c2 in real_serpy.__mro__:

                try:
                    self.assertEqual(c.__name__, c2.__name__)
                except AssertionError as err:
                   pass
                else:
                    pass
                if c.__name__ == c2.__name__:
                    equal_.append((c.__name__, c2.__name__))
                else:
                    not_equal.append((c.__name__, c2.__name__))
        equal_ = set(equal_)
        not_equal = set(not_equal)

    def test_final(self):
        f = self.Foo()
        original = self.FooSerializer(f, label='Serpy Serializer')
        copied = self.MySerializer(f, label='Modified Serializer')
        self.assertEqual(original.data, copied.data)

from serpy_mini import (Field, MethodField, BoolField,
                        FloatField, StrField, IntField,
                        Serializer)

class TestFields(unittest.TestCase):

    def test_to_value_noop(self):
        self.assertEqual(Field().to_value(5), 5)
        self.assertEqual(Field().to_value('a'), 'a')
        self.assertEqual(Field().to_value(None), None)

    def test_as_getter_none(self):
        self.assertEqual(Field().as_getter(None, None), None)

    def test_is_to_value_overrriden(self):
        class TransField(Field):
            def to_value(self, value):
                return value

        field = Field()
        self.assertFalse(field.to_value_overridden())
        field = TransField()
        self.assertTrue(field.to_value_overridden())
        field = IntField()
        self.assertTrue(field.to_value_overridden())

    def test_str_field(self):
        field = StrField()
        self.assertEqual(field.to_value('a'), 'a')
        self.assertEqual(field.to_value(5), '5')

    def test_bool_field(self):
        field = BoolField()
        self.assertTrue(field.to_value(True))
        self.assertFalse(field.to_value(False))
        self.assertTrue(field.to_value(1))
        self.assertFalse(field.to_value(0))

    def test_int_field(self):
        field = IntField()
        self.assertEqual(field.to_value(5), 5)
        self.assertEqual(field.to_value(5.4), 5)
        self.assertEqual(field.to_value('5'), 5)

    def test_float_field(self):
        field = FloatField()
        self.assertEqual(field.to_value(5.2), 5.2)
        self.assertEqual(field.to_value('5.5'), 5.5)

    def test_method_field(self):
        class FakeSerializer(object):
            def get_a(selfl, obj):
                return obj.a

            def z_sub_1(self, obj):
                return obj.z -1

        serializer = FakeSerializer()
        fn = MethodField().as_getter('a', serializer)
        self.assertEqual(fn(Obj(a=3)), 3)

        fn = MethodField('z_sub_1').as_getter('a', serializer)
        self.assertEqual(fn(Obj(z=3)), 2)
        self.assertTrue(MethodField.getter_flag)

    def test_field_label(self):
        field1 = StrField(label="@id")
        self.assertEqual(field1.label, "@id")


class TestSerializer(unittest.TestCase):

    def test_simple(self):
        class ASerializer(Serializer):
            a = Field()

        a = Obj(a=5)
        self.assertEqual(ASerializer(a).data['a'], 5)

    def test_data_cached(self):
        class ASerializer(Serializer):
            a = Field()

        a = Obj(a=5)
        serializer = ASerializer(a)
        data1 = serializer.data
        data2 = serializer.data
        # Use assertTrue instead of assertIs for python 2.6.
        self.assertTrue(data1 is data2)

    def test_inheritance(self):
        class ASerializer(Serializer):
            a = Field()

        class CSerializer(Serializer):
            c = Field()

        class ABSerializer(ASerializer):
            b = Field()

        class ABCSerializer(ABSerializer, CSerializer):
            pass

        a = Obj(a=5, b='hello', c=100)
        self.assertEqual(ASerializer(a).data['a'], 5)
        data = ABSerializer(a).data
        self.assertEqual(data['a'], 5)
        self.assertEqual(data['b'], 'hello')
        data = ABCSerializer(a).data
        self.assertEqual(data['a'], 5)
        self.assertEqual(data['b'], 'hello')
        self.assertEqual(data['c'], 100)

    def test_many(self):
        class ASerializer(Serializer):
            a = Field()

        objs = [Obj(a=i) for i in range(5)]
        data = ASerializer(objs, many=True).data
        self.assertEqual(len(data), 5)
        self.assertEqual(data[0]['a'], 0)
        self.assertEqual(data[1]['a'], 1)
        self.assertEqual(data[2]['a'], 2)
        self.assertEqual(data[3]['a'], 3)
        self.assertEqual(data[4]['a'], 4)

    def test_serializer_as_field(self):
        class ASerializer(Serializer):
            a = Field()

        class BSerializer(Serializer):
            b = ASerializer()

        b = Obj(b=Obj(a=3))
        self.assertEqual(BSerializer(b).data['b'].a, 3)

    def test_serializer_as_field_many(self):
        class ASerializer(Serializer):
            a = Field()

        class BSerializer(Serializer):
            b = ASerializer(many=True)

        b = Obj(b=[Obj(a=i) for i in range(3)])
        b_data = BSerializer(b).data['b']
        self.assertEqual(len(b_data), 3)
        self.assertEqual(b_data[0].a, 0)
        self.assertEqual(b_data[1].a, 1)
        self.assertEqual(b_data[2].a, 2)

    def test_serializer_as_field_call(self):
        class ASerializer(Serializer):
            a = Field()

        class BSerializer(Serializer):
            b = ASerializer(call=True)

        b = Obj(b=lambda: Obj(a=3))
        self.assertEqual(BSerializer(b).data['b'].a, 3)

    def test_serializer_method_field(self):
        class ASerializer(Serializer):
            a = MethodField()
            b = MethodField('add_9')

            def get_a(self, obj):
                return obj.a + 5

            def add_9(self, obj):
                return obj.a + 9

        a = Obj(a=2)
        data = ASerializer(a).data
        self.assertEqual(data['a'], 7)
        self.assertEqual(data['b'], 11)

    def test_to_value_called(self):
        class ASerializer(Serializer):
            a = IntField()
            b = FloatField(call=True)
            c = StrField(attr='foo.bar.baz')

        o = Obj(a='5', b=lambda: '6.2', foo=Obj(bar=Obj(baz=10)))
        data = ASerializer(o).data
        self.assertEqual(data['a'], 5)
        self.assertEqual(data['b'], 6.2)
        self.assertEqual(data['c'], '10')

    def test_serializer_with_custom_output_label(self):
        class ASerializer(Serializer):
            context = StrField(label='@context')
            content = MethodField(label='@content')

            def get_content(self, obj):
                return obj.content

        o = Obj(context='http://foo/bar/baz/', content='http://baz/bar/foo/')
        data = ASerializer(o).data

        self.assertIn('@context', data)
        self.assertEqual(data['@context'], 'http://foo/bar/baz/')
        self.assertIn('@content', data)
        self.assertEqual(data['@content'], 'http://baz/bar/foo/')


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result


if __name__ == '__main__':
    run_tests(Test)
    run_tests(TestFields)
    run_test(TestSerializer)