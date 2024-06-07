from bank import value


def test_value():
    assert(value("Hello")) == 0
    assert(value("Hello, world")) == 0
    assert(value("hi, hello")) == 20
    assert(value("..")) == 100
    assert(value("213214")) == 100
    assert(value("helo")) == 20
    assert(value("good morning")) == 100
