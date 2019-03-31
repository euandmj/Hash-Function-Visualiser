import json
import math
import os
import psutil
import mpu.io

MASK_8bit = 0xFFFFFFFF
MASK_32bit = 0xFFFFFFFFFFFFFFFF

# bitshift left
def leftrotate(b, n):
    b &= MASK_8bit
    return ((b << n) | (b >> (32 - n))) & MASK_8bit
    
def toHex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

class MD5:
    def __init__(self):
        self.rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                               5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
                               4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                               6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
        self.T = [int(abs(math.sin(i + 1)) * 2**32) & MASK_8bit for i in range(64)]
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

    def Hash(self, msg, load_from_file=False, write_to_file=True):
        assert((msg is str) == False), "MD5 function expected bytes, received %s" % (type(msg))

        if load_from_file:
            plaintext = msg
            # load the file using the msg as directory
            with open(msg[0], "rb") as f:
                msg = f.read()
        else:
            # parse ascii to bytes
            plaintext = msg
            msg = bytes(msg, encoding="utf-8")

        self.json_data.clear()

        # md5 buffers
        # moved into function due to 
        # weird runtime error of variable usage before initialisation 
        a0 = self.a0
        b0 = self.b0
        c0 = self.c0
        d0 = self.d0

        count = 0

        msg = bytearray(msg)
        length = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF
        # add 1
        msg.append(0x80)

        while len(msg) % 64 != 56: 
            msg.append(0)

        msg += length.to_bytes(8, byteorder='little')

        # for each 64 bit chunk
        for j in range(0, len(msg), 64):
            chunk = msg[j : j + 64]

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
                #calc rotatory
                ff = f # saved output of aux func for visual data
                M = int.from_bytes(chunk[4*g: 4*g+4], byteorder='little') # 4 bit m chunk
                rota = A + f + self.T[i] + M
                bb = (B + leftrotate(rota, self.rotate_amounts[i])) & MASK_8bit
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
                        "i": i,
                        "Buffers": [A, B, C, D],
                        "F": ff,
                        "M": M,
                        "S": rota,
                        "T": self.T[i],
                    }
                }
                self.json_data.append(data)
                    
            a0 = (a0 + A) & MASK_8bit
            b0 = (b0 + B) & MASK_8bit
            c0 = (c0 + C) & MASK_8bit
            d0 = (d0 + D) & MASK_8bit

        # append finally orignal message, padded block and the result
        self.json_data.insert(0, {
            "Message": plaintext,
            "Block": ''.join('{:02x}'.format(b) for b in msg),
            "Result": toHex(sum(val << (32 * i) for i, val in enumerate([a0, b0, c0, d0])))
        })

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
    
    def writeJsonFile(self):
        pass

    def Aux_Func(self, t, B, C, D):
        if 0 <= t <= 19:
            return (B & C) | (~B & D)
        elif 20 <= t <= 39:
            return B ^ C ^ D
        elif 40 <= t <= 59:
            return (B & C) | (B & D) | (C & D)
        else:
            return B ^ C ^ D
    
    def K(self, t):
        if 0 <= t <= 19:
            return 0x5A827999
        elif 20 <= t <= 39:
            return 0x6ED9EBA1
        elif 40 <= t <= 59:
            return 0x8F1BBCDC
        else:
            return 0xCA62C1D6

    def Hash(self, msg, load_from_file=False, write_to_file=True):
        assert((msg is str) == False), "MD5 function expected bytes, received %s" % (type(msg))
        
        if load_from_file:
            plaintext = msg
            # load the file using the msg as directory
            with open(msg[0], "rb") as f:
                msg = f.read()
        else:
            # parse ascii to bytes
            plaintext = msg
            msg = bytes(msg, encoding="utf-8")

        H0 = self.H0
        H1 = self.H1
        H2 = self.H2
        H3 = self.H3
        H4 = self.H4
       
        msg = bytearray(msg)

        length = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF

        # pad
        msg.append(0x80)
        while len(msg) % 64 != 56: 
            msg.append(0)

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
            f = self.Aux_Func(t, b, c, d)
            k = self.K(t)

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
        return '%08x%08x%08x%08x%08x' % (H0, H1, H2, H3, H4)
        #return toHex(sum(val << (32 * i) for i, val in enumerate([H0, H1, H2, H3, H4])))