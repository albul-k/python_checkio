"""
With this mission I want to start a series of missions with light bulbs. They will help you understand the concept of processes and evaluation of the processes’ performance. Instead of light bulbs, in real life, there may be equipment, the effectiveness of which must be calculated, or workers who go to work, and their wages must be calculated.

The first mission is quite simple. There is a light bulb, which by default is off, and a button, by pressing which the light bulb switches its state. This means that if the light bulb is off and the button is pressed, the light turns on, and if you press it again, it turns off.

The function input is an array of datetime objects - this is the date and time of pressing the button. Your task is to determine how long the light bulb has been turned on.

Input: A list of datetime objects

Output: A number of seconds as an integer.

Precondition:

The array of pressing the button is always sorted in ascending order
The array of pressing the button has no repeated elements (which means the result should always be bigger than 0)
The amount of elements is always even (the light will eventually be off)
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31
"""

from datetime import datetime
from typing import List

def sum_light(els: List[datetime]) -> int:
    res = 0
    for idx,itm in enumerate(els):
        if idx & 1 != 0:
            res += int((els[idx] - els[idx-1]).total_seconds())
    return res


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 12, 10 , 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 13, 11, 0 , 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")