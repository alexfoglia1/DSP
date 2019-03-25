import sys
gamma = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def clean(message):
    plaintext = message.lower()
    for ch in message:
        if ch not in gamma:
            plaintext = message.replace(ch,'')
    return plaintext

def indexof(aset,anelem):
    for i in range(0,len(aset)):
        if aset[i] == anelem:
            return i
    return -1

def extend_key(key,size):
    extkey = key
    i = 0
    while len(extkey)<=size:
        extkey = extkey + key[i%len(key)]
        i = i + 1
    return extkey

def encrypt(message, key):
    message = clean(message)
    size = len(message)
    extkey = extend_key(key,size)
    cipher = ''
    for i in range(0,size):
        m_i = indexof(gamma,message[i])
        k_i = indexof(gamma,extkey[i])
        sum_mod = (m_i+k_i)%len(gamma)
        cipher = cipher + gamma[sum_mod]
    return cipher

def decrypt(message, key):
    message = clean(message)
    size = len(message)
    extkey = extend_key(key,size)
    plaintext = ''
    for i in range(0,size):
        m_i = indexof(gamma,message[i])
        k_i = indexof(gamma,extkey[i])
        sum_mod = (m_i-k_i)%len(gamma)
        plaintext = plaintext + gamma[sum_mod]
    return plaintext

if __name__ == '__main__':
	key = clean("secretkey")
	message = "filippo xander ma non dica stronzate"
	enc = encrypt(message,key)
	dec = decrypt(enc,key)
	print("Original  message:\t"+message)
	print("Encrypted message:\t"+enc)
	print("Decrypted message:\t"+dec)
	exit()
