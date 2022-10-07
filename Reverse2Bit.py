R = ["CGT","CGC","CGA","CGG","AGA","AGG"]
P = ["CCT","CCC","CCA", "CCG"]
twoBit = ["00","01","10","11"]

def DNA2bin(DNA):
    binResult = ""
    bin2DnaMap = {"00": "A", "01": "T", "10": "G", "11": "C"}

    for dnaBase in DNA:
        for key in bin2DnaMap:
            if (bin2DnaMap[key] == dnaBase):
                binResult += key
    return binResult

def bin2ASCII(bin):
    ascii_text = ""
    binary_int = int(bin, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return (binary_int,ascii_text)

for r in R:
    for p in P:
        for bits in twoBit:
            ascii_text = ""
            bin = DNA2bin(r) + DNA2bin(p) + bits
            # print(f'bin: {bin}, \t r: {bin[0:7]} \t p: {bin[7:]}')
            dec_1,ascii_1 = bin2ASCII(bin[0:7])
            dec_2,ascii_2 = bin2ASCII(bin[7:])
            if ((dec_1 + dec_2)%14 == 0):
                print(f'{ascii_1}{ascii_2}')


