
from challenges.is_even import is_even


def test_is_even():
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(123456) == True
    assert is_even(654321) == False