import hashlib
from HashLib import MD5, SHA1
import random
import string

m = MD5()
s = SHA1()

print("running md5 test...")
for i in range(500):
    st = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    b = bytes(st, encoding="utf-8")
    assert(m.Hash(b) == hashlib.md5(b).hexdigest()), print(i)
print("md5 test passed.")

print("running sha1 test...")
for i in range(500):
    st = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    b = bytes(st, encoding="utf-8")
    assert(s.Hash(b) == hashlib.sha1(b).hexdigest()), print(i)
print("sha1 test passed.")