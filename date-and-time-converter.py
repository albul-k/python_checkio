"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

example

Input: Date and time as a string

Output: The same date and time, but in a more readable format

Precondition:
0 < date <= 31
0 < month <= 12
0 < year <= 3000
0 < hours < 24
0 < minutes < 60

"""

# solution #1
# from datetime import datetime
# def date_time(time: str) -> str:
#     inp = datetime.strptime(time, "%d.%m.%Y %H:%M")
#     res = inp.strftime("%-d %B %Y year %-H {} %-M {}").format("hour"+("s" if inp.hour != 1 else ""), "minute"+("s" if inp.minute != 1 else ""))
#     return res

# solution #2
# import datetime
# def date_time(time: str) -> str:
#     #replace this for solution
#     h = 'hours'
#     m = 'minutes'
#     if (datetime.datetime.strptime(time, '%d.%m.%Y %H:%M')).hour == 1:
#         h = 'hour'
#     if (datetime.datetime.strptime(time, '%d.%m.%Y %H:%M')).minute == 1:
#         m = 'minute'
#     return datetime.datetime.strptime(time, '%d.%m.%Y %H:%M').strftime('%-d %B %Y year %-H ' + h + ' %-M ' + m)


def date_time(time: str) -> str:
    month_dict = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    d, t = time.split()[0], time.split()[1]
    day = int(d.split('.')[0])
    month = month_dict[int(d.split('.')[1])]
    year = int(d.split('.')[2])
    hours = int(t.split(':')[0])
    if hours == 1:
        hours_w = 'hour'
    else:
        hours_w = 'hours'
    minites = int(t.split(':')[1])
    if minites == 1:
        minites_w = 'minute'
    else:
        minites_w = 'minutes'

    return f'{day} {month} {year} year {hours} {hours_w} {minites} {minites_w}'


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time(
        "01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time(
        "09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time(
        "20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
