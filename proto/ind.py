from rabin import *

def fastExp(base, exp, mod):
    d,c = 1,0
    binary = "{0:b}".format(exp)
    for digit in binary:
        d = (d**2) % mod
        if digit == '1':
            d = (d * base) % mod
    return d


def ind(alpha,p,a):
    i = 1
    while(True):
        print("test {}".format(i))
        if fastExp(alpha,i,p) == a:
            return i
        else:
            i = i + 1

alpha = 10**150
p = randPrime(alpha,alpha*10)
print(p)
i = p//2
e = (fastExp(alpha,i,p))
print(e)
print(ind(alpha,p,e))
