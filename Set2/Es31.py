import math as m
import random as r
import time as t

def extEuclide(a, b):
    r, r1, q, t = b,a,1,0
    while r1 != 0:
        temp,t = t,q
        floor = m.floor(r / r1)
        q = temp - floor * q
        temp = r
        r = r1
        r1 = temp - floor * r1
    if t < 0:
        t = t + b
    if r>1:
        t = None
    return int(r), int(t)
    
def fastExp(base, exp, mod):
    d,c = 1,0
    binary = "{0:b}".format(exp)
    for digit in binary:
        d = (d**2) % mod
        if digit == '1':
            d = (d * base) % mod
    return d

def even(n):
    return n%2 == 0

def checkModule(v, n):
    for _n in v[0:-1]:
        if _n % n == n - 1:
            return False
    return True

def rabinTest(x, n):
    _x,r,_m = [], 0, n-1
    while even(_m):
        _m = _m // 2
        r = r + 1
    _x.append(fastExp(x, _m, n))
    for i in range(0, r):
        _x.append(fastExp(_x[i], 2, n))
    return _x[0] != 1 and checkModule(_x, n) 


def randPrime(inf, sup, repeats):
    rnd = 0
    while True:
        rnd = r.randint(inf, sup)
        if not even(rnd):
            flag = True
            for i in range(0, repeats):
                if rabinTest(r.randint(2, sup),rnd):
                    flag = False
                    break
            if not flag:
                continue
            else:
                return rnd

               
def rsaKeyGen(p, q):
    n = p*q
    euler = (p-1)*(q-1)
    d = randPrime(2, n-1, 10)
    while extEuclide(d, euler)[0] != 1:
        d = randPrime(2,n-1, 10)
    e = extEuclide(d, euler)
    privateKey = (d, n)
    publicKey = (e[1], n)
    return privateKey,publicKey

def rsaKeyGenCRT(p, q):
    n = p * q
    euler = (p - 1) * (q - 1)
    d = randPrime(2, n - 1, 10)
    while d != 1 and extEuclide(d, euler)[0] != 1:
        d = randPrime(2, n-1, 20)
    _q = extEuclide(q, p)[1]
    _p = extEuclide(p, q)[1]
    e = extEuclide(d, euler)
    privateKey = (p, q, d, _p*p, _q*q)
    publicKey = (e[1], n)
    return privateKey, publicKey


rsaEncrypt = lambda plaintext, key: fastExp(plaintext, key[0], key[1])
rsaDecrypt = lambda ciphertext,key: fastExp(ciphertext, key[0], key[1])
rsaDecryptCRT = lambda ciphertext, privateKey: ((fastExp(ciphertext, privateKey[2], privateKey[0])\
                 * privateKey[4]) + (fastExp(ciphertext, privateKey[2], privateKey[1])\
                 * privateKey[3]))%(privateKey[0]*privateKey[1])
                 
def testSchemaCRT():
    print("**************RSA CRT**************")
    N = 150
    MIN = 10**N
    MAX = 10**(N+1)
    plaintext = r.randint(MIN,MAX)
    print("Original plaintext: {}".format((plaintext)))
    p = randPrime(MIN,MAX,10)
    q = randPrime(MIN,MAX,10)
    priv,pub = rsaKeyGenCRT(p,q)
    ciphertext = rsaEncrypt(plaintext,pub)
    print("Ciphertext: {}".format(ciphertext))
    dec = rsaDecryptCRT(ciphertext,priv)
    print("Deciphered plaintext: {}".format(dec))
    print("Deciphered = plaintext? -> {}".format(dec==plaintext))

def testSchemaSTD():
    print("**************RSA STD**************")
    N = 150
    MIN = 10**N
    MAX = 10**(N+1)
    plaintext = r.randint(MIN,MAX)
    print("Original plaintext: {}".format((plaintext)))
    p = randPrime(MIN,MAX,10)
    q = randPrime(MIN,MAX,10)
    priv,pub = rsaKeyGen(p,q)
    ciphertext = rsaEncrypt(plaintext,pub)
    print("Ciphertext: {}".format(ciphertext))
    dec = rsaDecrypt(ciphertext,priv)
    print("Deciphered plaintext: {}".format(dec))
    print("Deciphered = plaintext? -> {}".format(dec==plaintext))

def testOnCasualCiphertexts():
    print("*************COMPARISON*************")
    N = 150
    MIN = 10**N
    MAX = 10**(N+1)
    p = randPrime(MIN,MAX,10)
    q = randPrime(MIN,MAX,10)
    ciphertexts = []
    exectimestd = []
    exectimecrt = []
    for i in range(0,100):
        ciphertexts.append(r.randint(MIN,MAX))
    priv,pub = rsaKeyGen(p,q)
    privCRT,pubCRT = rsaKeyGenCRT(p,q)
    for c in ciphertexts:
        t0 = t.time()
        rsaDecrypt(c,priv)
        exectimestd.append(t.time()-t0)
        t0 = t.time()
        rsaDecryptCRT(c,privCRT)
        exectimecrt.append(t.time()-t0)
    maxstd = max(exectimestd)
    minstd = min(exectimestd)
    totstd = sum(exectimestd)
    avgstd = totstd/100
    maxcrt = max(exectimecrt)
    mincrt = min(exectimecrt)
    totcrt = sum(exectimecrt)
    avgcrt = totcrt/100
    diffmax = maxcrt-maxstd
    diffmin = mincrt-minstd
    difftot = totcrt-totstd
    diffavg = avgcrt-avgstd
    print("Standard RSA\tTotal time (sec)\tMaximum time (sec)\tMinimum time (sec)\tAverage time (sec)")
    print("\t\t{}\t{}\t{}\t{}\n".format(totstd,maxstd,minstd,avgstd))
    print("CRT RSA\t\tTotal time (sec)\tMaximum time (sec)\tMinimum time (sec)\tAverage time (sec)")
    print("\t\t{}\t{}\t{}\t{}\n".format(totcrt,maxcrt,mincrt,avgcrt))
    print("Difference\t{}\t{}\t{}\t{}".format(difftot,diffmax,diffmin,diffavg))
    print("\t\t({})%\t({})%\t({})%\t({})%".format((100*difftot)/totstd,(100*diffmax)/maxstd,(100*diffmin)/minstd,(100*diffavg)/avgstd))

if __name__ == '__main__':
    testSchemaSTD()
    testSchemaCRT()
    testOnCasualCiphertexts()



    
