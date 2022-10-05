

from challenges.remove_duplicates import remove_duplicates_fn, remove_duplicates


def test_remove_duplicate():
    assert remove_duplicates([1,2,3,2,4,6,2,6,7]) == [1,2,3,4,6,7]
    assert remove_duplicates_fn([1,2,3,2,4,6,2,6,7]) == [1,2,3,4,6,7]