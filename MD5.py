import math
import struct
import numpy
from bitarray import bitarray

# sine table
T = [64]

# MD5 Buffers
WORD_A = [0x01, 0x23, 0x45, 0x67]
WORD_B = [0x89, 0xab, 0xcd, 0xef]
WORD_C = [0xfe, 0xdc, 0xba, 0x98]
WORD_D = [0x76, 0x54, 0x32, 0x10]

def BfferBArray(A):
    # Given a 4x8 bit hex value A 
    # - format to a 32bit bitstring
    b = bitarray()
    for byte in A:
        b.extend('{0:08b}'.format(byte))
    return b


s = [   7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22, 
        5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
        4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
        6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 ]

def leftshift(b, n):
    return b[n:] + (bitarray('0') * n)

string = "Hello world"

bArray = ''.join(format(ord(x), 'b') for x in string)
bArray = bitarray(bArray)


######### pad message ############
bArray.append(True)
while bArray.length() % 512 != 448:
    bArray.append(0)

# len is 448. - append 64 bit length of original message
lengthbits = "{0:b}".format(len(string))
b = bitarray(lengthbits)

while b.length() < 64:
    b.append(0)

for bit in b:
    bArray.append(bit)



######## Process Block ########

# construct sine table
for i in range(63):
    T.append(abs(math.sin(i+1)) * 2**32)

# copy block i into X
for j in range(16):
    # one of 16 32 bit words in the block
    X = bitarray()
    for x in range(16): 
        X.append(bArray[j * 16 + x]) 
        

    # copy buffers
    A = BfferBArray(WORD_A)
    B = BfferBArray(WORD_B)
    C = BfferBArray(WORD_C)
    D = BfferBArray(WORD_D)



    # main loop
    for  i in range(64):
        f = 0
        g = 0       

        if 0 <= i and i <= 15:
            f += (B & C) | (D & ~B)
            g += i
        elif 16 <= i and i <= 31:
            f += (D & B) | (~D & C)
            g += (5 * i + 1) % 16
        elif 32 <= i and i <= 47:
            f += B ^ C ^ D
            g += (3 * i + 5) % 16
        elif 48 <= i and i <= 63:
            f += C ^ (B | ~D)
            g += (7 * i) % 16
        
        f = f + A + T[i] + bArray[g]
        A = D
        D = C
        C = B
        B = B + leftshift(f, s[i])


