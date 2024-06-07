import pytest
from um import count

def test_count():
    assert(count("hello world") == 0)
    assert(count("umumumumum") == 0)
    assert(count("Well, Um, actually") == 1)
    assert(count("Um, thanks, um...") == 2)
    # assert(count() == )
    # assert(count() == )
