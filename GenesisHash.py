from math import floor

LEADING_ZERO = "0"


def remapASCII(ASCII):
    """
    95 Printable characters 32 - 126
    https://en.wikipedia.org/wiki/ASCII
    https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html

    Remaps ASCII value to some unique 12-14 digit value (Tested).
    """
    strASCII = str(ASCII)

    # Use string methods to separate ASCII digits
    if ASCII < 100:
        # Two digit ASCII values
        L_0 = LEADING_ZERO
        L_1, L_2 = strASCII
    else:
        # Three digit ASCII values
        L_0, L_1, L_2 = strASCII

    # Convert separate string digits back to int
    L_0 = int(L_0)
    L_1 = int(L_1)
    L_2 = int(L_2)

    """
    Before modulus:
        min = 29124297227663 (14 digits)
        max = 325620017749655509090396059873 (30 digits)
    """
    return floor(floor(((L_0+3)**10 + (L_1+3)**10)/3) /
                 (L_2+3))**3 % (10**14-1)


def append_even_string_index(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i]
    return int(result)


def sum_odd_string_index(str):
    result = 0
    for i in range(len(str)):
        if i % 2 != 0:
            result += int(str[i])
    return result


def strToRemappedASCII(string):
    resultASCII = ""
    for char in string:
        resultASCII += str(remapASCII(ord(char)))
    return resultASCII


password = "password"

remappedASCII_PW = strToRemappedASCII(password)
_hash = append_even_string_index(
    remappedASCII_PW) + sum_odd_string_index(remappedASCII_PW)

while _hash < 10**256:
    _hash = _hash**2

_hash = _hash % (10**256-1)

print(f'hash: {_hash}\n')
print(len(str(_hash)))
