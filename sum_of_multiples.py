"""Sum of multiples."""


def sum_mul(n, m):
    """Thi will return sum of multiples."""
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
