from twttr import shorten

def test_shorten():
    assert(shorten("aeiou")) == ""
    assert(shorten("AEIOU")) == ""
    assert(shorten("Twitter")) == "Twttr"
    assert(shorten("Hello, world")) == "Hll, wrld"
    assert(shorten("1a2d3c")) == "12d3c"
