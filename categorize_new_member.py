"""Kata: Categorize New Member.

Return a list that consist of string values Open or Senior.
Stating whether the respective member is to be placed
in the senior or open category.
"Best Practices" #1 solution.
"""


def open_or_senior(data):
    """."""
    output = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
    return output
