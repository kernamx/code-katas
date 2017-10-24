"""Test categorize new member."""
import pytest


# value = [(tuble), (tuble), (tuble)]
# inside of tuble should be input, output:  (input, output)
# if inside of tuble the input is a list and output should be a list too:  (
# [[], [], []], ['', '', ''])
# in this case we have a list of list of inputs and the a list of outputs:
# [([[], [], [], []], ['', '', '', '']), ([[], [], [], []], ['', '', '', ''])]

value = [([[45, 12], [55, 21], [19, -2], [104, 20]],
          ['Open', 'Senior', 'Open', 'Senior']),
         ([[16, 23], [73, 1], [56, 20], [1, -1]],
          ['Open', 'Open', 'Senior', 'Open'])]


@pytest.mark.parametrize('any_input, any_output', value)
def test_open_or_senior_55_21(any_input, any_output):
    """The function test is using parametrize method to run multiple inputs."""
    from categorize_new_member import open_or_senior
    assert open_or_senior(any_input) == any_output


def test_just_one_value():
    """The function test is using hard coding method."""
    from categorize_new_member import open_or_senior
    assert open_or_senior([[55, 21], [4, 5]]) == ['Senior', 'Open']
