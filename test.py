def rotateCircularArray(string,shift,direction="fwd"):
    """
    rotateCircularArray("apple",0) -> apple
    rotateCircularArray("apple",1) -> eappl
    rotateCircularArray("apple",2) -> leapp
    rotateCircularArray("apple",3) -> pleap
    """
    shiftedString=""
    length = len(string)
    shiftBy = shift % length

    if direction == "bwd":
        newStartIndex = shiftBy
    else:
        newStartIndex = length - shiftBy

    for i in range(length):
        newIndex = (newStartIndex + i) % length
        shiftedString += string[newIndex]
    return shiftedString

print(rotateCircularArray("apple",0))
print(rotateCircularArray("apple",1))
print(rotateCircularArray("apple",2))
print(rotateCircularArray("apple",3))