def intronSplicing(decimal, threshold=14):
    """
    5'-GU...AG-3'
    5'-1001...0010-3'
    5'-oeeo...eeoe-3'
    """
    strDecimal = str(decimal)
    dnaLen = len(strDecimal)
    if dnaLen >= 8:
        introns = []
        startRemove = -1
        endRemove = -1
        startFound = False
        endFound = False
        result = ""
        for i in range(dnaLen-7):
            # Start of Intron
            if (not startFound and
                int(strDecimal[i]) % 2 == 1 and
                int(strDecimal[i+1]) % 2 == 0 and
                int(strDecimal[i+2]) % 2 == 0 and
                    int(strDecimal[i+3]) % 2 == 1):
                startRemove = i
                startFound = True
                # print(f"Start: {startRemove}")
            # End of Intron
            if (startFound and
                int(strDecimal[i+4]) % 2 == 0 and
                int(strDecimal[i+5]) % 2 == 0 and
                int(strDecimal[i+6]) % 2 == 1 and
                    int(strDecimal[i+7]) % 2 == 0):
                endRemove = i+7
                endFound = True
                # print(f"End: {endRemove}")
            # Remove Intron
            if endFound:
                startFound = False
                endFound = False
                introns.append(strDecimal[startRemove:endRemove+1])
                # print(f'Intron: {strDecimal[startRemove:endRemove+1]}')
        for intron in introns:
            intronLen = len(intron)
            if (dnaLen-intronLen >= threshold):
                dnaLen -= intronLen
                strDecimal = strDecimal.replace(intron, "")

    return strDecimal


DNA = "31001777700104"
print(intronSplicing(DNA))
