"""
Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items, after which each element equals the median of the three elements in the original list ending in that position.

Wait...You don't know what the "median" is? Go check out the separate "Median" mission on CheckiO.

Input: Iterable of ints.

Output: Iterable of ints.

The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen

"""


from typing import Iterable
from statistics import median

def median_three(els: Iterable[int]) -> Iterable[int]:
    result: list = []
    for idx,itm in enumerate(els):
        if idx in [0, 1]:
            result.append(itm)
        else:
            value = median(els[idx-2:idx+1])
            result.append(value)
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    assert list(median_three([1])) == [1]
    assert list(median_three([5, 2, 9, 1, 7, 4, 6, 3, 8])) == [5, 2, 5, 2, 7, 4, 6, 4, 6]

    print("Coding complete? Click 'Check' to earn cool rewards!")
