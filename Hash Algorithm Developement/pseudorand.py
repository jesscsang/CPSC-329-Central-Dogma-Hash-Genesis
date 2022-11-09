from math import floor
from time import perf_counter

def pseudoRandom():
    """
    After running for one minute:
        ones digit: {0: 10092, 1: 10276, 2: 10094, 3: 10058, 4: 9916, 5: 10099, 6: 10007, 7: 10019, 8: 10080, 9: 10052}
    """
    return floor(perf_counter()**3)%10

# print(pseudoRandom())

ones_digit = {}

power = 3
while True:
    outcome_power = perf_counter()**power
    # print(floor(outcome_power))
    _1stDigit = floor(outcome_power)%10
    if _1stDigit in ones_digit:
        ones_digit[_1stDigit] += 1
    else:
        ones_digit[_1stDigit] = 1

    print(f'ones digit: {dict(sorted(ones_digit.items(), key=lambda item: item[0]))}')
