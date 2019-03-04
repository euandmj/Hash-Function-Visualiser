import math
import psutil
import json
import os

MASK_8bit = 0xFFFFFFFF

rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21] 

# auBillarC functions
def F(B, C, D):
    return (B & C) | (~B & D)

def G(B, C, D):
    return (B & D) | (C & ~D)

def H(B, C, D):
    return B ^ C ^ D

def I(B, C, D):
    return C ^ (B | ~D)
    
# bitshift left
def leftrotate(b, n):
    b &= 0xFFFFFFFF
    return ((b << n) | (b >> (32 - n))) & MASK_8bit
    
def toHex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))
   
def computeDigest(*buffers):
    #return sum(x << (32 * i)) for i, x in enumerate(buffers)[2:]
    return 2    

def writeJsonFile(data):
    import mpu.io
    # attempt to fix bug of only overwriting once per program instance
    if(os.path.exists('loop.json')):
        os.remove('loop.json')
    mpu.io.write('loop.json', data)

# sine constants
T = [int(abs(math.sin(i + 1)) * 2**32) & MASK_8bit for i in range(64)]
# md5 buffers
#a0 = 0x67452301   
#b0 = 0xefcdab89   
#c0 = 0x98badcfe   
#d0 = 0x10325476  


json_data = []


def MD5(msg):
    assert((msg is str) == False), "The input message is not a string."
    json_data.clear()
    # md5 buffers
    # moved into function due to 
    # weird runtime error of variable usage before initialisation 
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476
    plaintext = msg
  


    count = 0

    #convert string to bytearray
    #add some check for utf vs ascii 
    msg = bytes(msg, encoding="utf-8")
    msg = bytearray(msg)
    length = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF
    # add 128
    msg.append(0x80)

    while len(msg) % 64 != 56: msg.append(0)

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
            count += 1
            if 0 <= i <= 15:
                f = F(B, C, D)
                g = i
            if 16 <= i<= 31:
                f = G(B, C, D)
                g = (5 * i + 1) % 16
            if 32 <= i <= 47:
                f = H(B, C, D)
                g = (3 * i + 5) % 16
            if 48 <= i <= 63:
                f = I(B, C, D)
                g = (7 * i) % 16
            #calc rotatory             
            rota = A + f + T[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
            bb = (B + leftrotate(rota, rotate_amounts[i])) & MASK_8bit
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
                    "Rotate": rotate_amounts[i],
                    "f": f,
                    "g": g,
                    "T": T[i],
                }
            }
            json_data.append(data)


                
        a0 = (a0 + A) & MASK_8bit
        b0 = (b0 + B) & MASK_8bit
        c0 = (c0 + C) & MASK_8bit
        d0 = (d0 + D) & MASK_8bit

    # append finally orignal message, padded block and the result
    json_data.insert(0, {
        "Message": plaintext,
        "Block": ''.join('{:02x}'.format(b) for b in msg),
        "Result": toHex(sum(val << (32 * i) for i, val in enumerate([a0, b0, c0, d0])))
    })

    writeJsonFile(json_data)
    return sum(val << (32 * i) for i, val in enumerate([a0, b0, c0, d0]))


if __name__ == "__main__":
    digest = MD5("abc")
    print(toHex(digest))


    process = psutil.Process(os.getpid())
    print("Memory used %sMB" % (process.memory_info().rss / 1000000))