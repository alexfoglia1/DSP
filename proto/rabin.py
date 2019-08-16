import math as m
import random as r
from sys import argv

even = lambda n:n%2==0

def fastExp(base, exp, mod):
    d,c = 1,0
    binary = "{0:b}".format(exp)
    for digit in binary:
        d = (d**2) % mod
        if digit == '1':
            d = (d * base) % mod
    return d


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

def isPrime(n, alpha = 0.001):
    k = m.ceil(m.log2(1/alpha)/2)
    repeats = int(k)
    for i in range(0, repeats):
        if rabinTest(r.randint(2, n-1),n):
            return False
    return True
    
def randPrime(inf, sup, alpha = 0.001):
    while True:
        rnd = r.randint(inf, sup)
        rnd = rnd + 1
        if rnd > sup:
            rnd = rnd - 2
        if isPrime(rnd,alpha):
            return rnd

def detPrimeTest(n):
    if n==0:
        return False
    elif n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(3,int(n**0.5 + 1)):
            if n%i == 0:
                return False
        return True


if __name__ == '__main__':
    try:
        _min = int(eval(argv[1]))
        _max = int(eval(argv[2]))
    except:
        print("Usage: {} min max".format(argv[0]))
        exit()

        if _min < _max:
            n = randPrime(_min,_max)
        elif _max < _min:
            n = randPrime(_max,_min)
        else:
            if isPrime(_min):
                n = _min
            else:
                print("No primes between {} and {}".format(_min,_max))
                exit()
        print(n)

