from Es31 import *

def decryptionexp(n, d, e):
    _m = e*d - 1
    it = 0
    while even(_m):
        _m //= 2
    while True:
        it = it + 1
        x = randPrime(2, n, 10)
        v = fastExp(x, _m, n)
        if v == 1:
            continue
        while v != 1:
            v0, v = v, fastExp(v, 2, n)
        if v0 != -1 and v0 != n-1:
            return m.gcd(v0 + 1, n), it
            
def var(v):
    mean = sum(v)/len(v)
    copy = []
    for vi in v:
        copy.append((mean-vi)**2)
    return sum(copy)/len(copy)

def test():
    pq = []
    print("Generating p,q . . .")
    for i in range(0,100):
        pq.append((randPrime(10**150,10**151,10),randPrime(10**150,10**151,10)))
        print("{}-th step done".format(i))
    de = []
    for pair in pq:
        p = pair[0]
        q = pair[1]
        print("Generated n = {}".format(p*q))
        priv,pub = rsaKeyGen(p,q)
        print("Generated d = {}".format(priv[0]))
        print("Generated e = {}".format(pub[0]))
        de.append((priv[0],pub[0]))
    it = []
    times = []
    for i in range(0,100):
        n = pq[i][0]*pq[i][1]
        d = de[i][0]
        e = de[i][1]
        print("Testing on n = {} d = {} e = {}".format(n,d,e))
        t0 = t.time()
        res = decryptionexp(n,d,e)
        delta_t = t.time()-t0
        it.append(res[1])
        times.append(delta_t)
        print("Iterations: {}".format(res[1]))
        print("Elapsed time: {} sec".format(delta_t))
    avg_it = sum(it)/100
    avg_time = sum(times)/100
    print("****** Results ******")
    print("Avg it\tAvg time (s)\tVar time (s^2)")
    print("{}\t{}\t{}".format(avg_it,avg_time,var(times)))

if __name__ == '__main__':
    test()
    
            
