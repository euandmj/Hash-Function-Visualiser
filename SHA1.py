import struct
import math
import sys

# functions and constants

# auxillary functions
def Aux_Func(t, B,C,D):
    if 0 <= t <= 19:
        return (B & C) | (~B & D)
    elif 20 <= t <= 39:
        return B ^ C ^ D
    elif 40 <= t <= 59:
        return (B & C) | (B & D) | (C & D)
    elif 60 <= t <= 79:
        return B ^ C ^ D

# Sequence of constant words given loops t
def K(t):
    if 0 <= t <= 19:
        return 0x5A827999
    elif 20 <= t <= 39:
        return 0x6ED9EBA1
    elif 40 <= t <= 59:
        return 0x8F1BBCDC
    else:
        return 0xCA62C1D6



MASK_8bit = 0xFFFFFFFF

def leftrotate(b,n):
    return ((b << n) | (b >> (32 - n))) & MASK_8bit

    
def toHex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

def toHex2(digest):
    return b''.join(struct.pack(b'>I', h) for h in digest)


def SHA1(msg):
    assert((msg is str) == False), "The input message is not a string."

    # H Buffer definitions
    H0 = 0x67452301
    H1 = 0xEFCDAB89
    H2 = 0x98BADCFE
    H3 = 0x10325476
    H4 = 0xC3D2E1F0

    msg = bytes(msg, encoding='utf-8')
    msg = bytearray(msg)

    length = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF

    # pad
    msg.append(0x80)
    while len(msg) % 64 != 56: msg.append(0)

    msg += length.to_bytes(8, byteorder='little')

    for W in range(0, len(msg), 64):
        chunk = msg[W : W + 64]

        w = [0] * 80

        for i in range(16):
            w[i] = int.from_bytes(chunk[4*i: 4*i+4], byteorder='little')

        for t in range(16, 80):
            w[t] = leftrotate((w[t-3] ^ w[t - 8] ^ w[t - 14] ^ w[t - 16]), 1)

        #It was also shown that for the rounds 32–79 the computation of:
        # w[i] = (w[i-3] xor w[i-8] xor w[i-14] xor w[i-16]) leftrotate 1
        # can be replaced with:
        # w[i] = (w[i-6] xor w[i-16] xor w[i-28] xor w[i-32]) leftrotate 2
        # This transformation keeps all operands 64-bit aligned and,
        # by removing the dependency of w[i] on w[i-3],
        # allows efficient SIMD implementation with a vector length of 4 like x86 SSE instructions.        

        a, b, c, d, e = H0, H1, H2, H3, H4

        for t in range(80):
            f = Aux_Func(t, b, c, d)
            k = K(t)

            temp = (leftrotate(a, 5) + f + e + w[t] + k) & MASK_8bit
            
            e = d
            d = c
            c = leftrotate(b, 30)
            b = a
            a = temp

        H0 = (H0 + a) & MASK_8bit
        H1 = (H1 + b) & MASK_8bit
        H2 = (H2 + c) & MASK_8bit
        H3 = (H3 + d) & MASK_8bit
        H4 = (H4 + e) & MASK_8bit
    
    # After processing M(n), the message digest is the 160-bit string
    # represented by the 5 words
    #return '%08x%08x%08x%08x%08x' % (H0, H1, H2, H3, H4)
    return sum(val << (32 * i) for i, val in enumerate([H0, H1, H2, H3, H4]))




if __name__ == "__main__":
    digest = SHA1("abc")
    val = toHex(digest)
    print(val)