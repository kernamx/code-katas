"""Test Sum of multiples."""

import pytest


test_list = [([0, 0], 'INVALID'), ([2, 9], 20), ([4, -7], 'INVALID')]


@pytest.mark.parametrize('input, output', test_list)
def test_sum_mul(input, output):
    """Testing."""
    from sum_of_multiples import sum_mul
    assert sum_mul(input) == 'output'
    # assert sum_mul(0, 0) == 'INVALID'
    # assert sum_mul(4, -7) == 'INVALID'
