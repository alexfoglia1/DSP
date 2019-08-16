import time
import sys
import rabin

def isPrime(n):
    if n == 2:
        return True
    else:
        if useRabin:
            return rabin.isPrime(n)
        else:
            return detIsPrime(n)

def detIsPrime(n):
    for i in range(2, 1 + int(n**0.5)):
        if n % i == 0:
            return False
    return True

def factorize(n):
    N = n
    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    factors = []
    for p in primes:
        if n%p == 0:
            factors.append(p)
    return factors

N = int(sys.argv[1])
useRabin = ( int(sys.argv[2]) >= 1 )
N_IN = N
t0 = time.time()
factors = factorize(N)
delta = time.time()-t0
factorization = "{} = ".format(N)
for f in factors:
    while N % f == 0:
        t0 = time.time()
        N = N / f
        delta += (time.time()-t0)
        factorization = factorization + ( "{}*".format(f) )
factorization = factorization + "{}".format(N)
print("Factors of {}:\n{}".format(N_IN, factors))
print("\nFactorization:")
print(factorization)
print("\nTime elapsed: {} s".format(delta))
