from lab6.Huffman import *

file = "abdcfbae"
print("Original File:", file)

symbols = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [2, 2, 1, 1, 1, 1]
huff_code = HuffmanCode(symbols, freq)

code = huff_code.encoding
size = 0
print("Coding Scheme:")
for i in huff_code.encoding:
    print(i.symbol, "=", i.code)
    size += i.freq * len(i.code)

encoded_file = ""
for i in file:
    for j in code:
        if j.symbol == i:
            encoded_file += j.code
print("Encoded File:", encoded_file)

decoded_file = ""
i = 0
while i < size:
    j = 0
    s = ""
    loop = 1
    while loop and i+j < size:
        s += encoded_file[i+j]
        for k in code:
            if k.code == s:
                decoded_file += k.symbol
                loop = 0
                break
        j += 1
    i += j
print("Decoded File:", decoded_file)
