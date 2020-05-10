"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Precondition: elements can be ints or strings

The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
"""

# solution #1
# from collections import Counter
# def frequency_sort(items):
#     return sorted(Counter(items).elements(), key=lambda x: items.count(x), reverse=True)

# solution #2
# def frequency_sort(items):
#     return sorted(sorted(items, key=lambda item: items.index(item)), key=lambda item: items.count(item), reverse=True)

# solution #3
# def frequency_sort(items):
#     new_dict = {}
#     if len(items) == len(set(items)):
#         return items
#     else:
#         for item in items:
#             new_dict[item] = items.count(item)
#         result = sorted([[key] * value for key, value in new_dict.items()], key=len, reverse=True)
#         return [item for lst in result for item in lst]


def frequency_sort(items):
    if not len(items) > 0:
        return items

    list_keys, dict_keys = [], {}
    for itm in items:
        if dict_keys.get(itm) is None:
            dict_keys[itm] = items.count(itm)
            list_keys.append((itm, dict_keys[itm]))

    last_value = float("-inf")
    list_keys_sorted = []
    for itm in list_keys:
        if itm[1] > last_value:
            list_keys_sorted.insert(0, itm)
            last_value = itm[1]
        else:
            ins = False
            for ind, itm1 in enumerate(list_keys_sorted):
                if itm[1] > itm1[1]:
                    list_keys_sorted.insert(ind, itm)
                    ins = True
                    break
            if ins == False:
                list_keys_sorted.append(itm)

    list_result = []
    for itm in list_keys_sorted:
        for i in range(1, itm[1] + 1):
            list_result.append(itm[0])

    return list_result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
        4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
        'bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
