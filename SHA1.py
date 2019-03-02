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
    elif 60 <= t <= 79:
        return 0xCA62C1D6

# H Buffer definitions
H0 = 0x67452301
H1 = 0xEFCDAB89
H2 = 0x98BADCFE
H3 = 0x10325476
H4 = 0xC3D2E1F0

def leftrotate(b,n):
    b &= 0xFFFFFFFF
    return ((b << n) | (b >> (32 - n))) & 0xFFFFFFFF

    
def toHex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))


def SHA1(msg):
    assert((msg is str) == False), "The input message is not a string."

    msg = bytes(msg, encoding='utf-8')
    msg = bytearray(msg)

    length = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF
    
    # pad
    msg.append(0x80)
    while len(msg) % 64 != 56: msg.append(0)

    msg += length.to_bytes(8, byteorder='little')

    for W in range(0, len(msg), 64):
        chunk = msg[W : W + 64]

        for t in range(16, 80):
            W[t] = (W[t-6] ^ W[t - 16] ^ W[t - 28] ^ W[t - 32])
            W[t] = leftrotate(W[t], 2)


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

            temp = leftrotate(a, 5) + f + e + W[t] + K(t) & 0xFFFFFFFF
            
            e = d
            d = c
            c = leftrotate(b, 30)
            b = a
            a = temp

        H0 = (H0 + a) & 0xFFFFFFFF
        H1 = (H1 + b) & 0xFFFFFFFF
        H2 = (H2 + c) & 0xFFFFFFFF
        H3 = (H3 + d) & 0xFFFFFFFF
        H4 = (H4 + e) & 0xFFFFFFFF
    
    # After processing M(n), the message digest is the 160-bit string
    # represented by the 5 words
    return sum(val << (32 * i) for i, val in enumerate([H0, H1, H2, H3]))




if __name__ == "__main__":
    digest = SHA1("abc")
    val = toHex(digest)
    print(val)