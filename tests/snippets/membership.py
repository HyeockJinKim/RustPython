# test lists
assert 3 in [1, 2, 3]
assert 3 not in [1, 2]

assert not (3 in [1, 2])
assert not (3 not in [1, 2, 3])

# test strings
assert "foo" in "foobar"
assert "whatever" not in "foobar"

# test bytes
# TODO: uncomment this when bytes are implemented
# assert b"foo" in b"foobar"
# assert b"whatever" not in b"foobar"

# test tuple
assert 1 in (1, 2)
assert 3 not in (1, 2)

# test set
# TODO: uncomment this when sets are implemented
# assert 1 in set(1, 2)
# assert 3 not in set(1, 2)

# test dicts
# TODO: test dicts when keys other than strings will be allowed
assert "a" in {"a": 0, "b": 0}
assert "c" not in {"a": 0, "b": 0}

# test iter
assert 3 in iter([1, 2, 3])
assert 3 not in iter([1, 2])

# test sequence
# TODO: uncomment this when ranges are usable
# assert 1 in range(0, 2)
# assert 3 not in range(0, 2)

# test __contains__ in user objects
class MyNotContainingClass():
    pass


try:
    1 in MyNotContainingClass()
except TypeError:
    pass
else:
    assert False, "TypeError not raised"


class MyContainingClass():
    def __init__(self, value):
        self.value = value

    def __contains__(self, something):
        return something == self.value


assert 2 in MyContainingClass(2)
assert 1 not in MyContainingClass(2)