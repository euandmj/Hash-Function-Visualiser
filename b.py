from bitstring import BitArray

a = BitArray(bin='1001')
b = BitArray(bin='1111')
c = a & b
print(c)