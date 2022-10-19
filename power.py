from math import floor

ones_digit = {}
twos_digit = {}
threes_digit = {}
power = 3
for i in range (1,1000):
    outcome_power = i**power
    print(floor(outcome_power))
    _1stDigit = floor(outcome_power)%10
    if _1stDigit in ones_digit:
        ones_digit[_1stDigit] += 1
    else:
        ones_digit[_1stDigit] = 1

    _2ndDigit = floor(outcome_power/10)%10
    if _2ndDigit in twos_digit:
        twos_digit[_2ndDigit] += 1
    else:
        twos_digit[_2ndDigit] = 1

    _3rdDigit = floor(floor(outcome_power/10)/10)%10
    if _3rdDigit in threes_digit:
        threes_digit[_3rdDigit] += 1
    else:
        threes_digit[_3rdDigit] = 1

print(f'ones digit: {dict(sorted(ones_digit.items(), key=lambda item: item[0]))}')
print(f'twos digit: {dict(sorted(twos_digit.items(), key=lambda item: item[0]))}')
print(f'threes digit: {dict(sorted(threes_digit.items(), key=lambda item: item[0]))}')