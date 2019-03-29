#This is the code of Exercise 3.2
#It depends upon library numpy, available with pip: launch pip install numpy if missing
#In order to execute the code, user has to launch python3 hill.py
#
#Author: Alex Foglia, 6336805

import numpy
import math
from numpy import matrix
from numpy import linalg
from itertools import *

gamma = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def indexof(letter): #utility function used to get the index of a letter within the alphabet gamma
    for i in range(0,len(gamma)):
        if letter == gamma[i]:
            return i
    return -1

def clean(text): #utility function used to clean a text as requested
    cln = text.lower()
    for ch in text:
        if ch not in gamma:
            cln = cln.replace(ch,'')
    return cln

def dot_product(mat, vec): #compute the dot product between a matrix and a vector
    p = len(gamma)
    res = []
    for row in mat:
        if len(row)!=len(vec):
            raise ValueError("Size of mat is different from size of vec")
        res_i = 0
        for i in range(0,len(row)):
            res_i = res_i + row[i]*vec[i]
        res.append(res_i%p)
    return res

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
    n=len(A)
    A=matrix(A)
    adj=numpy.zeros(shape=(n,n))
    for i in range(0,n):
      for j in range(0,n):
        adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
    return (__modInv__(int(round(linalg.det(A))),p)*adj)%p

def __modInv__(a,p):          # Finds the inverse of a mod p, if it exists (note that a is a number)
    for i in range(1,p):
      if (i*a)%p==1:
        return i
    raise ValueError(str(a)+" has no inverse mod "+str(p))


def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
    A=numpy.array(A) # Convert A to numpy.array class
    minor=numpy.zeros(shape=(len(A)-1,len(A)-1)) #constructing minor matrix
    p=0
    for s in range(0,len(minor)):
      if p==i:
          p=p+1
      q=0
      for t in range(0,len(minor)):
          if q==j:
              q=q+1
          minor[s][t]=A[p][q]
          q=q+1
      p=p+1
    return minor

def create_indexes(block): #create a vector of index foreach block
    indexes = []
    for ch in block:
        indexes.append(indexof(ch))
    return indexes

def create_characters(ciphervalues): #from a block of index it creates a vector of characters
    chars = []
    for val in ciphervalues:
        chars.append(gamma[int(val)])
    return ''.join(chars)

def cipher_block(plainblock, key): #function which encrypt a block
    blockvalues = create_indexes(plainblock) #create index value of characters
    ciphervalues = dot_product(key, blockvalues) #compute dot product between plaintext indexes and the key
    cipherblock = create_characters(ciphervalues) #get back to ciphered characters
    return cipherblock

def encrypt(text, key): #function which encrypt a text
    text = clean(text) #clean text
    m = len(key)
    blocks = []
    cipherblocks = []
    for i in range(0,len(text),m): #we divide text in block of length equal to the key size
        blocks.append(text[i:i+m])
    if len(blocks[-1])!= m: #padding last block if it is too short
        for i in range(len(blocks[-1]),m):
            blocks[-1] = blocks[-1] + 'a'
    for block in blocks: #foreach block it constructs a ciphered message composed of the result of ciphering each block with the same key
        cipherblocks.append(cipher_block(block,key))
    return ''.join(cipherblocks)

def decrypt(text, key): #just an invocation of encrypt with the inverse key matrix
    key = modMatInv(key, len(gamma))
    return encrypt(text,key)

def shiftLeft(v): #compute the left shift of a vector
    temp = v[0]
    for i in range(0,len(v)-1):
        v[i] = v[i+1]
    v[-1] = temp

def find_key(pt, ct, m): #Crack hill cipher: pt,ct shall be list of indexes, m is the key size
    pairs = []
    for i in range(0,len(pt),m):
        pairs.append((create_indexes(pt[i:i+m]),create_indexes(ct[i:i+m]))) #pairs will be a list of pairs (plaintext,ciphertext)
    if len(pairs) < m:
        raise Exception("Too few pairs of plaintext ciphertext")
    k = 0 # counter for number of shift
    while k < len(pairs):
        pstar = []
        cstar = []
        for i in range(0,m):
            pstar.append(pairs[i][0]) #P* is a m x m matrix in which each line is known plaintext
            cstar.append(pairs[i][1]) #C* is a m x m matrix in which cstar[i] = ciphertext(plaintext[i])
        try:
            key = dot_product(numpy.transpose(cstar),modMatInv(numpy.transpose(pstar),len(gamma))) #as in textbook, matrix shall be transposed wrt to the one computed yet
            print("!!FOUND THE KEY!!")
            return key
        except:
            shiftLeft(pairs) #Shift left vector of pairs plaintext,ciphertext and the next iteration will refresh P* and C*
            k = k + 1
    return None

def key2str(key): #utility function which prints out a matrix
    k2s = []
    for row in key:
        k2srow = ''
        for val in row:
            k2srow = k2srow + str(val) + ' '
        k2s.append(k2srow)
    return str(k2s).replace(",","\r\n").replace("[","\r\n").replace("]","")

if __name__ == '__main__': #main code
    txt = clean("Il cifrario di Hill risulta vulnerabile ad attacchi di tipo known plaintext") #example of a plaintext
    key = [ [1,2,3,2]
           ,[1,1,4,3]
           ,[1,1,1,7]
           ,[1,2,1,1] ] #example of a 4 x 4 key
    ciphertext = encrypt(txt,key) #encryption of ciphertext
    print("Input text: "+txt) #print input text
    print("Ciphertext: "+ciphertext) #print ciphertext
    decrypted = decrypt(ciphertext,key) #print regular decryption assuming that we know the key
    print("Decrypted: "+decrypt(ciphertext,key))
    print("*********** ATTACKING HILL CIPHER ***********")
    guessed_key = find_key(txt,ciphertext,len(key)) #call crack hill routine
    if guessed_key is not None: #if the key is found, then:
        print("Decryption of ciphertext using the guessed key:" + key2str(guessed_key)) #test decryption
        print(decrypt(ciphertext,guessed_key))
    else:
        print("No suitable pairs of plaintext,ciphertext")

