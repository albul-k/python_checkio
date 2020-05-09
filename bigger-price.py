"""
You have a table with all available goods in the store. The data is represented as a list of dicts

Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given as a first argument and the whole data as the second one

Input: int and list of dicts. Each dicts has two keys "name" and "price"

Output: the same as the second Input argument.
"""


def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    last_price = float("-inf")
    goods_sorted = []
    for itm in data:
        if itm['price'] > last_price:
            goods_sorted.insert(0, itm)
            last_price = itm['price']
        else:
            ins = False
            for ind, itm1 in enumerate(goods_sorted):
                if itm['price'] > itm1['price']:
                    goods_sorted.insert(ind, itm)
                    ins = True
                    break
            if ins == False:
                goods_sorted.append(itm)

    return goods_sorted[0:limit]


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "meat", "price": 20},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
