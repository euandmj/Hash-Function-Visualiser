import json
import math
import os
import psutil
import mpu.io
from struct import unpack

BITMASK_8 = 0xFFFFFFFF
BITMASK_32 = 0xFFFFFFFFFFFFFFFF

# bitshift b left by n


def leftrotate(b, n):
    b &= BITMASK_8
    return ((b << n) | (b >> (32 - n))) & BITMASK_8


def toHex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))


def loadFromFile(filepath):
    try:
        with open(filepath, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print("file not found\n%s" % filepath)
    except Exception as e:
        print(e)


class MD5:
    def __init__(self):
        self.rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                               5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
                               4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                               6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
        self.T = [int(abs(math.sin(i + 1)) * 2**32)
                  & BITMASK_8 for i in range(64)]
        self.a0 = 0x67452301
        self.b0 = 0xefcdab89
        self.c0 = 0x98badcfe
        self.d0 = 0x10325476
        self.json_data = []

    def writeJsonFile(self, data):
        filepath = "loop.json"
        # attempt to fix bug of only overwriting once per program instance
        if os.path.isfile(filepath):
            os.remove(filepath)
        mpu.io.write(filepath, data)

    def Hash(self, msg, write_to_file=True):
        assert isinstance(
            msg, bytes), "MD5 function expected bytes, received %s" % type(msg)

        # if load_from_file:
        #     plaintext = msg
        #     # load the file using the msg as directory
        #     msg = loadFromFile(msg)
        # else:
        #     # parse ascii to bytes
        #     plaintext = msg
        #     msg = bytes(msg, encoding="utf-8")


        plaintext = msg.decode("utf-8")

        self.json_data.clear()
        header = {}

        # md5 buffers
        # moved into function due to
        # weird runtime error of variable usage before initialisation
        a0 = self.a0
        b0 = self.b0
        c0 = self.c0
        d0 = self.d0

        count = 0

        msg = bytearray(msg)
        header["Message"] = plaintext
        header["RawBytes"] = ''.join('{:b}'.format(b) for b in msg)
        length = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF
        
        # add 1
        msg.append(0x80)
        header["RawBytes1"] = ''.join('{:b}'.format(b) for b in msg)

        # add 0s
        while len(msg) % 64 != 56:
            msg.append(0)
        header["RawBytes0"] = ''.join('{:b}'.format(b) for b in msg)

        msg += length.to_bytes(8, byteorder='little')
        header["Block"] = ''.join('{:b}'.format(b) for b in msg)

        # for each 64 bit chunk
        for j in range(0, len(msg), 64):
            chunk = msg[j: j + 64]

            A = a0
            B = b0
            C = c0
            D = d0

            # main loop
            for i in range(64):
                count += 1
                if 0 <= i <= 15:
                    # aux func F
                    f = (B & C) | (~B & D)
                    g = i
                if 16 <= i <= 31:
                    # aux func G
                    f = (B & D) | (C & ~D)
                    g = (5 * i + 1) % 16
                if 32 <= i <= 47:
                    # aux func H
                    f = B ^ C ^ D
                    g = (3 * i + 5) % 16
                if 48 <= i <= 63:
                    # aux func I
                    f = C ^ (B | ~D)
                    g = (7 * i) % 16
                # calc rotatory

                # visual data save point
                vdata = {
                    "i": i,
                    "Buffers": [A, B, C, D],
                    "F": f,
                    "T": self.T[i]
                }

                # int value from the 4 byte chunk
                M = int.from_bytes(chunk[4*g: 4*g+4], byteorder='little')

                rota = A + f + self.T[i] + M
                bb = (B + leftrotate(rota, self.rotate_amounts[i])) & BITMASK_8
                A = D
                D = C
                C = B
                B = bb

                # construct json file
                data = {
                    "Loop": {
                        "Id": count,
                        "Word": ''.join('{:02x}'.format(b) for b in chunk),
                        "Buffers": [A, B, C, D],
                        "Rotate": self.rotate_amounts[i],
                        "f": f,
                        "g": g
                    },
                    "VisualData": {
                        "i": vdata["i"],
                        "Buffers": vdata["Buffers"],
                        "BuffersNew": [A, B, C, D],
                        "F": vdata["F"],
                        "M": M,
                        "S": self.rotate_amounts[i],
                        "T": self.T[i]
                    }
                }
                self.json_data.append(data)

            a0 = (a0 + A) & BITMASK_8
            b0 = (b0 + B) & BITMASK_8
            c0 = (c0 + C) & BITMASK_8
            d0 = (d0 + D) & BITMASK_8
        
        self.json_data.insert(0, header)

        if write_to_file:
            self.writeJsonFile(self.json_data)
        # return the combination of the 4 buffers, converted to big endian hex
        return toHex(sum(val << (32 * i) for i, val in enumerate([a0, b0, c0, d0])))


class SHA1:
    def __init__(self):
        # H Buffer definitions
        self.H0 = 0x67452301
        self.H1 = 0xEFCDAB89
        self.H2 = 0x98BADCFE
        self.H3 = 0x10325476
        self.H4 = 0xC3D2E1F0
        self.json_data = []

    def writeJsonFile(self):
        filepath = "loop.json"
        # attempt to fix bug of only overwriting once per program instance
        if os.path.isfile(filepath):
            os.remove(filepath)
        mpu.io.write(filepath, self.json_data)

    def F(self, t, B, C, D):
        if 0 <= t <= 19:
            return (B & C) | (~B & D)
        if 20 <= t <= 39:
            return B ^ C ^ D
        if 40 <= t <= 59:
            return (B & C) | (B & D) | (C & D)
        if 60 <= t <= 79:
            return B ^ C ^ D

        print("Error sha1 aux func overflow")
        return 0

    def K(self, t):
        if 0 <= t <= 19:
            return 0x5A827999
        if 20 <= t <= 39:
            return 0x6ED9EBA1
        if 40 <= t <= 59:
            return 0x8F1BBCDC
        if 60 <= t <= 79:
            return 0xCA62C1D6

        print("Error sha1 K func overflow")
        return 0

    def Hash(self, msg, write_to_file=True):
        assert isinstance(
            msg, bytes), "SHA1 function expected bytes, received %s" % type(msg)


        # plaintext is the decoded msg
        plaintext = msg.decode("utf-8")


        # if load_from_file:
        #     plaintext = msg
        #     # load the file using the msg as directory
        #     msg = loadFromFile(msg[0])
        # else:
        #     # parse ascii to bytes
        #     plaintext = msg
        #     msg = bytes(msg, encoding="utf-8")


        header = {}
        H0 = self.H0
        H1 = self.H1
        H2 = self.H2
        H3 = self.H3
        H4 = self.H4
        count = 0
        msg = bytearray(msg)

        header["Message"] = plaintext
        header["RawBytes"] = ''.join('{:b}'.format(b) for b in msg)

        length = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF

        # pad
        # add 1
        msg.append(0x80)
        header["RawBytes1"] = ''.join('{:b}'.format(b) for b in msg)
        
        # add 0s
        while len(msg) % 64 != 56:
            msg.append(0)
        header["RawBytes0"] = ''.join('{:b}'.format(b) for b in msg)
        
        # add length
        msg += length.to_bytes(8, byteorder='big')
        header["Block"] = ''.join('{:b}'.format(b) for b in msg)

        # RFC method 1
        # parse msg[i] into 16 32 bit words (512 block)
        for M in range(0, len(msg), 64):
            W = list(unpack('>16L', msg[M:M+64]))

            #  a. Divide M(i) into 16 words W(0), W(1), ... , W(15), where W(0)
            #   is the left-most word.
            for i in range(16, 80):
                W.append(leftrotate((W[i-3] ^ W[i-8] ^ W[i-14] ^ W[i-16]), 1))

            a,b,c,d,e = H0, H1, H2, H3, H4

            for i in range(0, 80):
                f = self.F(i, b, c, d)
                k = self.K(i)               

                # json data
                vdata = {
                    "i": i,
                    "Buffers": [a, b, c, d, e],
                    "F": f,
                    "W": 0,
                    "K": k
                } 
                
                a, b, c, d, e = leftrotate(a, 5) + f + e + k + W[i] & BITMASK_8, \
                    a, leftrotate(b, 30), c, d
               
                # final json data
                data = {
                    "Loop": {
                        "Id": count,
                        "Word": ''.join('{:02x}'.format(b) for b in W),
                        "Buffers": [a, b, c, d, e],
                        "f": f,
                        "g": k
                    },
                    "VisualData": {
                        "i": vdata["i"],
                        "Buffers": vdata["Buffers"],
                        "BuffersNew": [a, b, c, d, e],
                        "F": vdata["F"],
                        "W": W[i],
                        "K": k
                    }
                }
                self.json_data.append(data)
                count += 1

            H0 = (H0 + a) & BITMASK_8
            H1 = (H1 + b) & BITMASK_8
            H2 = (H2 + c) & BITMASK_8
            H3 = (H3 + d) & BITMASK_8
            H4 = (H4 + e) & BITMASK_8

        self.json_data.insert(0, header)
        # write the json
        if write_to_file:
            self.writeJsonFile()        

        # After processing M(n), the message digest is the 160-bit string
        # represented by the 5 words
        return '%08x%08x%08x%08x%08x' % (H0, H1, H2, H3, H4)

if __name__ == "__main__":
    # s = SHA1()
    # b = s.Hash("foo", write_to_file=False)
    # print(b)
    pass
