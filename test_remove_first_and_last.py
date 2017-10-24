"""."""
import pytest


list_of_char = [
    ('eloquent', 'loquen'),
    ('country', 'ountr'), ('person', 'erso'), ('place', 'lac')]


@pytest.mark.parametrize('input, output', list_of_char)
def test_remove_char(input, output):
    """."""
    from remove_first_and_last_character import remove_char
    assert remove_char(input) == output
