import math

rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21] 

# auxillary functions
def F(X, Y, Z):
    return (X & Y) | (~X & Z)

def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)

def H(X, Y, Z):
    return X ^ Y ^ Z

def I(X, Y, Z):
    return Y ^ (X | ~Z)
    
# bitshift left
def leftrotate(b, n):
    b &= 0xFFFFFFFF
    return ((b << n) | (b >> (32 - n))) & 0xFFFFFFFF    
    
def toHex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))
   
def computeDigest(*buffers):
    #return sum(x << (32 * i)) for i, x in enumerate(buffers)[2:]
    return 2    

# sine const
T = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

# md5 buffers
#a0 = 0x67452301   
#b0 = 0xefcdab89   
#c0 = 0x98badcfe   
#d0 = 0x10325476   

message = "fuck fuck fuck"

def MD5(msg):
    # md5 buffers
    a0 = 0x67452301   
    b0 = 0xefcdab89   
    c0 = 0x98badcfe   
    d0 = 0x10325476   

    msg = bytearray(msg)
    length = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF
    msg.append(0x80)

    while len(msg) % 512 != 448: msg.append(0)

    msg += length.to_bytes(8, byteorder='little')

    # for each 32 bit word
    for j in range(0, len(msg), 64):
        chunk = msg[j : j + 64]

        A = a0
        B = b0
        C = c0
        D = d0

        # main loop
        for i in range(64):
            if 0 <= i and i <= 15:
                f = F(B, C, D)
                g = i
            if 16 <= i and i <= 31:
                f = G(B, C, D)
                g = (5 * i + 1) % 16
            if 32 <= i and i <= 47:
                f = H(B, C, D)
                g = (3 * i + 5) % 16
            if 48 <= i and i <= 63:
                f = I(B, C, D)
                g = (7 * i) % 16
            rota = A + f + T[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
            bb = (B + leftrotate(rota, rotate_amounts[i])) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = bb
        
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF       
    return a0   



result = b"abc"

digest = MD5(result)
#digest = toHex(digest)



print(digest)