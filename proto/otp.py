from vigenere import *
import random as r

def rand_int(max):
    return int(r.random()*max)

def otp(message, key, fun):
    message = clean(message)
    cipher = ''
    for i in range(0,len(key)):
        k = key[i]
        pt = indexof(gamma,message[i])
        sum_mod = fun(k,pt)%len(gamma)
        cipher = cipher + gamma[sum_mod]
    return cipher

def keygen(message):
    key = []
    for i in range(0,len(message)):
        key.append(rand_int(100))
    return key

message = "example"
key = keygen(message)
enc = otp(message,key,lambda x,y:x+y)
dec = otp(enc,key,lambda x,y:x-y)
print("Original message: "+message)
print("OTP encrypted message: "+enc)
print("OTP decrypted message: "+dec)
