from bitarray import bitarray

def bitstring_toString(b):
    s = ""
    for bit in b:
        s += "1" if bit is True else "0"
    return s

def bin_add(*args): return bin(sum(int(x, 2) for x in args))[2:]

x = bitarray('1111')
y = bitarray('1001')

xs = bitstring_toString(x)
ys = bitstring_toString(y)

z = bin_add(xs, ys)
print(z)