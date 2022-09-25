
def stringToBin(string):
    resultBin = ""
    for char in string:
        resultBin += bin(ord(char))[2:]
    return resultBin


def strToASCII(string):
    resultASCII = ""
    for char in string:
        resultASCII += str(ord(char)) + " "
    return resultASCII


def binToDNA(bin):
    DNA_Result = ""
    bin2DnaMap = {"00": "A", "01": "G", "10": "C", "11": "T"}

    for i in range(0, len(bin)-1, 2):
        binaryPair = bin[i]+bin[i+1]

        for key in bin2DnaMap:
            if (key == binaryPair):
                DNA_Result += bin2DnaMap[key]

    return DNA_Result


def compStrand(DNA):
    compStrand = ""
    basePairing = {"A": "T", "G": "C"}

    for dnaBase in DNA:
        for key in basePairing:
            if (basePairing[key] == dnaBase):
                compStrand += key
            if (key == dnaBase):
                compStrand += basePairing[key]
    return compStrand


def DNA2bin(DNA):
    binResult = ""
    bin2DnaMap = {"00": "A", "01": "T", "10": "G", "11": "C"}

    for dnaBase in DNA:
        for key in bin2DnaMap:
            if (bin2DnaMap[key] == dnaBase):
                binResult += key
    return binResult


def RNA2aminoAcids(RNA):
    aaResult = ""
    RNA_Codons = {
        # 'M' - START, '_' - STOP
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "UGU": "C", "UGC": "C",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "UUU": "F", "UUC": "F",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "CAU": "H", "CAC": "H",
        "AUA": "I", "AUU": "I", "AUC": "I",
        "AAA": "K", "AAG": "K",
        "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "AUG": "M",
        "AAU": "N", "AAC": "N",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "UGG": "W",
        "UAU": "Y", "UAC": "Y",
        "UAA": "", "UAG": "", "UGA": ""
    }

    print(RNA)
    for i in range(0, len(RNA)-2, 3):
        rnaCodon = RNA[i]+RNA[i+1]+RNA[i+2]
        for key in RNA_Codons:
            if (key == rnaCodon):
                aaResult += RNA_Codons[key]
    return aaResult


def postTranscriptMod(RNA):
    matureRNA = ""
    for i in range(RNA):
        if (RNA[i]+RNA[i+1] == "GU"):
            pass
        if (RNA[i]+RNA[i+1] == "AG"):
            pass


def formatChar(string, groupsOf):
    result = ""
    counter = 0
    for char in string:
        result += char
        counter += 1
        if counter == groupsOf:
            result += " "
            counter = 0
    return result


def CentralDogmaHash(string):
    return RNA2aminoAcids(compStrand(binToDNA('0'+DNA2bin(compStrand(binToDNA(stringToBin(string))[::-1]))+'0')).replace('T', 'U'))


password = "Hello World"
print(CentralDogmaHash(password))

# binaryPW = stringToBin(password)
# binModify = "0" + binaryPW + "0"


# print(f"0. Password: \n\t {password}")
# print(f"1. Password => ASCII: \n\t {strToASCII(password)}")
# print(f"2. ASCII => Binary: \n\t {formatChar(stringToBin(password),8)}")
# print(
#     f"3. Binary => DNA Coding Strand: \n\t 3'-{formatChar(binToDNA(binaryPW),10)}-5'")
# print(
#     f"4. Reverse DNA Coding Strand: \n\t 5'-{formatChar(binToDNA(binaryPW)[::-1],10)}-3'")
# print(
#     f"5. DNA Coding Strand => DNA Template Strand: \n\t 3'-{formatChar(compStrand(binToDNA(binaryPW)[::-1]),10)}-5'")
# print(
#     f"6. DNA Template Strand => Binary: \n\t {formatChar(DNA2bin(compStrand(binToDNA(binaryPW)[::-1])),10)}")
# print(
#     f"7. Add Zeros to Both Ends: \n\t {formatChar('0'+DNA2bin(compStrand(binToDNA(binaryPW)[::-1]))+'0',10)}")
# print(
#     f"8. Binary => DNA Template Strand: \n\t 3'-{formatChar(binToDNA('0'+DNA2bin(compStrand(binToDNA(binaryPW)[::-1]))+'0'),10)}-5'")
# print(
#     f"9. DNA Template Strand => DNA Coding Strand: \n\t 5'-{formatChar(compStrand(binToDNA('0'+DNA2bin(compStrand(binToDNA(binaryPW)[::-1]))+'0')),10)}-3'")
# print(
#     f"10. DNA Coding Strand => mRNA: \n\t 5'-{formatChar(compStrand(binToDNA('0'+DNA2bin(compStrand(binToDNA(binaryPW)[::-1]))+'0')).replace('T','U'),10)}-3'")
# print(
#     f"11. mRNA => AA: \n\t NH2-{formatChar(RNA2aminoAcids(compStrand(binToDNA('0'+DNA2bin(compStrand(binToDNA(binaryPW)[::-1]))+'0')).replace('T','U')),10)}-COOH")
