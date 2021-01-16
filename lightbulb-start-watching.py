"""
This is the second mission in the lightbulb series. I will try to make each following task slightly more complex.

You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit. Now let's add one more parameter - the counting start time.

This means that the light continues to turn on and off as before. But now, as a result of the function, I want not only to know how long there was light in the room, but how long the room was lit, starting from a certain moment.

One more argument is added – start_watching , and if it’s not passed, we count as in the previous version of the program for the entire period.

Input: Two arguments and only the first one is required. The first one is a list of datetime objects and the second one is a datetime object.

Output: A number of seconds as an integer.

Precondition:

The array of pressing the button is always sorted in ascending order
The array of pressing the button has no repeated elements
The amount of elements is always even (the light will eventually be off)
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31
"""

from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    res = 0
    for idx,itm in enumerate(els):
        if idx & 1 != 0:
            if start_watching is None or els[idx-1] > start_watching:
                res += int((els[idx] - els[idx-1]).total_seconds())
            elif start_watching >= els[idx-1] and els[idx] >= start_watching:
                res += int((els[idx] - start_watching).total_seconds())
    return res


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 5)))
    
    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    start_watching=datetime(2015, 1, 12, 10, 0, 5)) == 5
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], datetime(2015, 1, 12, 10, 0, 0)) == 10
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 0)) == 610
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 10)) == 600
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 10, 10, 0)) == 620

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 12, 10, 10),
    ], datetime(2015, 1, 12, 12, 10, 10)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 12, 10, 10),
    ], datetime(2015, 1, 12, 12, 9, 10)) == 60
    
    print("The second mission in series is done? Click 'Check' to earn cool rewards!")