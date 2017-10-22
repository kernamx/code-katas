"""Test categorize new member."""
import pytest


# open_or_senior1 = (
#     [[45, 12], [55, 21], [19, -2], [104, 20]],
#     ['Open', 'Senior', 'Open', 'Senior']
# )


# open_or_senior2 = (
#     [[16, 23], [73, 1], [56, 20], [1, -1]],
#     ['Open', 'Open', 'Senior', 'Open']
# )


# @pytest.mark.parametrize([age, handicap], open_or_senior1)
def test_open_or_senior_45_12():
    """."""
    from categorize_new_member import open_or_senior
    assert open_or_senior(45, 12) == 'Open'
