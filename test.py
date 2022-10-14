# 33 - 126
# https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html

from math import floor


def remapASCII(ASCII):
    strASCII = str(ASCII)

    # Use string methods to separate ASCII digits
    if ASCII < 100:
        # Two digit ASCII values
        L_0 = "0"
        L_1, L_2 = strASCII
    else:
        # Three digit ASCII values
        L_0, L_1, L_2 = strASCII

    # Convert separate string digits back to int
    L_0 = int(L_0)
    L_1 = int(L_1)
    L_2 = int(L_2)

    return floor(floor(((L_0+3)**10 + (L_1+3)**10)/3)/(L_2+3))**3


hashes = {}
for asciiVal in range(33, 127):

    _hash = remapASCII(asciiVal)

    # print(_hash)

    if _hash in hashes:
        # Increment the count of an existing hash by 1
        hashes[_hash] += 1
    else:
        # Add the new hash to the dictionary with count 1 in the
        # following format
        # "hash": "count"
        hashes[_hash] = 1

print(sorted(hashes.keys()))
# min = 29124297227663
# max = 325620017749655509090396059873
print(dict(sorted(hashes.items(), key=lambda item: item[1])))
