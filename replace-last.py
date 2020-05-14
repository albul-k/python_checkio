"""
In a given list the last element should become the first one. An empty list or list with only one element should stay the same

example

Input: List.

Output: Iterable.
"""

from typing import Iterable


def replace_last(items: list) -> Iterable:
    if len(items) == 0:
        return []
    _t = items.pop(-1)
    items.insert(0, _t)
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_last([2, 3, 4, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last([1])) == [1]
    assert list(replace_last([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
