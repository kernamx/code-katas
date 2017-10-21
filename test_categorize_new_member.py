"""Test categorize new member."""
import pytest


test.assert_equals(
    openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]),
    ['Open', 'Senior', 'Open', 'Senior']
)

test.assert_equals(
    openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]),
    ['Open', 'Open', 'Senior', 'Open']
)


def test_open_or_senior([age, handicap], [result]):
    """."""
    from categorize_new_member import open_or_senior
    assert open_or_senior(data) == result
