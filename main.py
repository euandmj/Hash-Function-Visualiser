import math
import struct
import numpy
from bitarray import bitarray

def bitarray_toString(b):
    s = ""
    for bit in b:
        s += "1" if bit is True else "0"
    return s

def bin_add(*args): return bin(sum(int(x, 2) for x in args))[2:]

# auxillary functions
def F(X, Y, Z):
    return (X & Y) | (~X & Z)

def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)

def H(X, Y, Z):
    return X ^ Y ^ Z

def I(X, Y, Z):
    return Y  (X ^ ~Z)

# sine table
T = [64]
# sine table in binary
Tb = [64]

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

def leftshift(b, n):
    return b[n:] + (bitarray('0') * n)

# Round 1 
def Round1(A, B, C, D, X, T):
    def Logic(a, b, c, d, k, s, i):
        # a = b + ((a + F(b,c,d) + X[k] + T[i]) <<< s)
        # abcd = 32 bit strings
        # make X[k] and T[i] equal 32 bit strings too
        x = '{0:032b}'.format(X[k]) # format to 32bit string.
        #t = ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', T[i])) # 32 bit formatted float
        t = Tb[i]

        # parse to bitarrays
        xb = bitarray(str(x))
        tb = bitarray(str(t))
        f = F(b,c,d)

        val = bin_add(bitarray_toString(a), bitarray_toString(f), bitarray_toString(xb), t)
        x = len(val)
        val = bin_add(bitarray_toString(b), val)
        x = len(val)
        val = leftshift(bitarray(val), s)    
        x = len(val)
        #value = b & ((a & F(b,c,d) & xb & tb)) # value always turns false
        #val = bin(int(b, 2)) + ((bin(int(a,2)) + bin(int(F(b,c,d), 2)) + bin(int(X[k], 2)) + bin(int(T[i], 2))) << s)            
        
        #val = bin(int(b.tostring(), 2)) + bin(int(a.tostring(), 2)) % 2**32
        return val        
    
    A = Logic(A, B, C, D, 0, 7, 1)
    D = Logic(D, A, B, C, 1, 12, 2)
    C = Logic(C, D, A, B, 2, 17, 3)
    B = Logic(B, C, D, A, 3, 22, 4)

    A = Logic(A, B, C, D, 4, 7, 5)  
    D = Logic(D, A, B, C, 5, 12, 6)
    C = Logic(C, D, A, B, 6, 17, 7)
    B = Logic(B, C, D, A, 7, 22, 8)

    A = Logic(A, B, C, D, 8, 7, 9)
    D = Logic(D, A, B, C, 9, 12, 10)
    C = Logic(C, D, A, B, 10, 17, 11)
    B = Logic(B, C, D, A, 11, 22, 12)

    A = Logic(A, B, C, D, 12, 7, 13)
    D = Logic(D, A, B, C, 13, 12, 14)
    C = Logic(C, D, A, B, 14, 17, 15)
    B = Logic(B, C, D, A, 15, 22, 16)

    print(A)

def Round2(A, B, C, D, X, T):
    def logic(a, b, c, d, k, s, i):
          #a = b + ((a + G(b,c,d) + X[k] + T[i]) <<< s).  
        x = '{0:032b}'.format(X[k])
        t = ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', T[i]))
        # parse to bitarrays
        xb = bitarray(str(x))
        tb = bitarray(str(t))

        value = b & ((a + G(b,c,d) + xb, tb))
        value = leftshift(value, s)
        return value
        
    A = logic(A, B, C, D, 1, 5, 17)
    D = logic(D, A, B, C, 6, 9, 18)
    C = logic(C, D, A, B, 11, 14, 19)
    B = logic(B, C, D, A, 0, 20, 20)

    A = logic(A, B, C, D, 5, 5, 21)

    

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

# read in binary sin table
with open('sin.txt') as fp:
    Tb = [l.rstrip('\n') for l in fp]

# copy block i into X
for j in range(16):
    # one of 16 32 bit words in the block
    X = bitarray()
    for x in range(16): 
        X.append(bArray[j * 16 + x]) 
        

    A = BfferBArray(WORD_A)
    B = BfferBArray(WORD_B)
    C = BfferBArray(WORD_C)
    D = BfferBArray(WORD_D)
    
    # Round 1
    Round1(A, B, C, D, X, T)
