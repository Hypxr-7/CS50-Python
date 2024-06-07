from numb3rs import validate

def test_validate_input():
    assert(validate("0.0.0.0")) == True
    assert(validate("255.255.255.255")) == True
    assert(validate("123.112.23.3")) == True
    assert(validate("123.256.12.1")) == False
    assert(validate("123.-1.231.3")) == False

def test_validate_value_type():
    assert(validate("123.122.123")) == False
    assert(validate("123.3422.21.2.3")) == False
    assert(validate("W.132.43.12")) == False
    assert(validate("12.121.12:1")) == False
