from timeit import Timer
import HashLib
import psutil

def test(file):    
    m = HashLib.MD5()
    m.Hash(file)
    # print(o)

t1 = Timer("""test("t_1k")""", """from __main__ import test""")
print("1k: %s" % t1.timeit(10))
print(psutil.cpu_percent())

t1 = Timer("""test("t_10k")""", """from __main__ import test""")
print("10k: %s" % t1.timeit(1))
print(psutil.cpu_percent())

t1 = Timer("""test("t_100k")""", """from __main__ import test""")
print("100k: %s" % t1.timeit(1))
print(psutil.cpu_percent())

t1 = Timer("""test("t_1000k")""", """from __main__ import test""")
print("1000k: %s" % t1.timeit(1))
print(psutil.cpu_percent())

t1 = Timer("""test("t_10000k")""", """from __main__ import test""")
print("10000k: %s" % t1.timeit(1))
#print(psutil.cpu_percent())

# t1 = Timer("""test("t_100000k")""", """from __main__ import test""")
# print("100000k: %s" % t1.timeit(1))
# print(psutil.cpu_percent())