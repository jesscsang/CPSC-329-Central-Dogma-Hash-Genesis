from math import floor


def remappedASCII(ASCII):
    """
    95 Printable characters 32 - 126
    https://en.wikipedia.org/wiki/ASCII
    https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html

    Remaps ASCII value to some unique 12-14 digit value (Tested).
    """
    LEADING_ZERO = "0"

    strASCII = str(ASCII)

    # Use string methods to separate ASCII digits
    if ASCII < 10:
        # Single digit ASCII values
        L_0 = L_1 = LEADING_ZERO
        L_2 = strASCII
    elif ASCII < 100:
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
                 (L_2+3))**3 % (10**14)


remappedASCII_Vals = {}
for ASCII_Val in range(32, 127):

    newASCII_Val = remappedASCII(ASCII_Val)
    # newASCII_Val = len(str(remappedASCII(ASCII_Val)))

    # print(newASCII_Val)

    if newASCII_Val in remappedASCII_Vals:
        # Increment the count of an existing hash by 1
        remappedASCII_Vals[newASCII_Val] += 1
    else:
        # Add the new hash to the dictionary with count 1 in the
        # following format
        # "hash": "count"
        remappedASCII_Vals[newASCII_Val] = 1

print(sorted(remappedASCII_Vals.keys()))
# print(sorted(len(str(remappedASCII_Vals.keys()))))

# min = 29124297227663
# max = 325620017749655509090396059873
# print(dict(sorted(remappedASCII_Vals.items(), key=lambda item: item[1])))
