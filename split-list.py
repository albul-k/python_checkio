"""
You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.

example

Input: Array.

Output: Array or two arrays.
"""


def split_list(items: list) -> list:
    len_second = len(items) // 2
    len_first = len(items) - len_second
    first, second = [], []
    for i in range(0, len_first):
        first.append(items[i])
    for i in range(len_first, len(items)):
        second.append(items[i])
    return [first, second]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))
    print(split_list([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
