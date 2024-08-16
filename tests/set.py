import pytest

from objson import objson


def test_simpleset():
    obj = objson({})

    obj.foo = 4

    assert "foo" in obj and obj.foo == 4

    obj.foo = [1, 2, 3]

    assert obj.foo == [1, 2, 3]

    obj.foo = None  # still valid
    assert "foo" in obj and obj.foo is None

    del obj.foo  # this actually deletes it
    assert "foo" not in obj


def test_setitem():
    obj = objson({})

    obj["foo"] = 4

    assert "foo" in obj and obj.foo == 4


def test_set_nested_not_working():
    obj = objson({})

    with pytest.raises(AttributeError):
        obj.foo.bar = 42
