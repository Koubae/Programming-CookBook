import pytest

counter = 0

def add_counter():
    global counter
    counter += 1

# ---------------------------
# yield fixtures (recommended)
# ---------------------------


@pytest.fixture
def get_counter():
    print(f"{counter}) -- Fixture (yield)")
    add_counter()
    yield counter


def test_count_is_1(get_counter):
    assert get_counter == 1

def test_count_is_2(get_counter):
    assert get_counter == 2

# ---------------------------
# Adding finalizers directly
# ---------------------------

@pytest.fixture
def get_counter_direct(request):
    print(f"{counter}) -- Fixture (request)")
    add_counter()

    request.addfinalizer(add_counter)
    return counter

def test_count_is_3(get_counter_direct):
    assert get_counter_direct == 3