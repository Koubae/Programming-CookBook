import pytest

counter = 0

def add_counter():
    global counter
    counter += 1

# ---------------------------
# Module Level Setup/TearDown
# ---------------------------
def setup_module(module):
    """setup any state specific to the execution of the given module."""
    add_counter()
    print(f"{counter}) -- SetUp (module)")

def teardown_module(module):
    """teardown any state that was previously setup with a setup_module method."""
    add_counter()
    print(f"{counter}) -- tearDown (module)")

class TestSomeClass:

    # ---------------------------
    # Class level setup/teardown
    # ---------------------------
    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class (which usually contains tests)."""
        add_counter()
        print(f"{counter}) -- SetUp (class)")

    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a call to setup_class. """
        add_counter()
        print(f"{counter}) -- tearDown (class)")

    # ---------------------------
    # Class level setup/teardown
    # ---------------------------
    def setup_method(self, method):
        """setup any state tied to the execution of the given method in a class.  setup_method is invoked for every test method of a class."""
        add_counter()
        print(f"{counter}) -- SetUp (method)")

    def teardown_method(self, method):
        """teardown any state that was previously setup with a setup_method call. """
        add_counter()
        print(f"{counter}) -- tearDown (method)")

    def test_is_1_a_number(self):
        assert (1).__class__ is int


# ---------------------------
# module level  setup/teardown
# ---------------------------
def setup_function(function):
    """setup any state tied to the execution of the given function. Invoked for every test function in the module."""
    add_counter()
    print(f"{counter}) -- SetUp (function)")


def teardown_function(function):
    """teardown any state that was previously setup with a setup_function call."""
    add_counter()
    print(f"{counter}) -- tearDown (function)")

def test_something_at_module_level():
    assert (1).__class__ is int