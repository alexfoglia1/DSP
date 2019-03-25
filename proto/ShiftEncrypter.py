from gamma import *
import sys

def shift_encrypt(text, key):
    text = clean(text)
    ciphertext = ''
    for ch in text:
        i = indexof(gamma, ch)
        i = (i+key)%len(gamma)
        ciphertext = ciphertext + gamma[i]
    return ciphertext

def shift_decrypt(text, key):
    text = clean(text)
    plaintext = ''
    for ch in text:
        i = indexof(gamma, ch)
        i = (i-key)%len(gamma)
        plaintext = plaintext + gamma[i]
    return plaintext

if __name__ == '__main__':
    text = "example of an english text"
    key = 7
    ciphertext = shift_encrypt(text,key)
    print("Input text: "+text)
    print("Cipher text: "+ciphertext)
    print("Decrypted: "+shift_decrypt(ciphertext,key))

