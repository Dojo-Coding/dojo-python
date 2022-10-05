

from challenges.reverse_string import reverse_string


def test_reverse_string():
    result: str = reverse_string("Hello World")
    assert result == "dlroW olleH"