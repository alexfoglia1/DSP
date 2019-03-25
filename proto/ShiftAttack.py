from ShiftEncrypter import *
english_freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]

def create_vector(matrix, index):
    column = []
    for row in matrix:
        column.append(row[index%len(row)])
    return ''.join(column)

def create_freq_vector(line, gamma):
    freq = []
    for ch in gamma:
        c = float(count(ch,line))/float(len(line))
        freq.append(c/100.0)
    return freq
    
def count(ch, line):
    c = 0
    for letter in line:
        if letter == ch:
            c = c+1
    return c

def dot_product(v1, v2):
    if len(v1) != len(v2):
        print "v1 and v2 must be equally length"
        return None
    else:
        p = 0
        for i in range(0,len(v1)):
            p = p + (v1[i]*v2[i])
        return p
        
def shiftLeft(v):
    temp = v[0]
    for i in range(0,len(v)-1):
        v[i] = v[i+1]
    v[-1] = temp

def crackShift(Vi,gamma):
    m_max = 0
    index_max = 0
    for j in range(0,len(gamma)):
        m_g = dot_product(Vi,english_freq)
        if m_g > m_max:
            m_max = m_g
            index_max = j
        shiftLeft(Vi)
    return((m_max,index_max,gamma[index_max]))
    
if __name__ == '__main__':
    text = "example of a secret but sufficiently long english plain text"
    key = 4
    ciphertext = shift_encrypt(text,key)
    print("Input text: "+text)
    print("Cipher text: "+ciphertext)
    print("Decrypted: "+shift_decrypt(ciphertext,key))
    print("*********** SHIFT ATTACK ***********")
    Vi = create_freq_vector(ciphertext,gamma)
    key = (crackShift(Vi,gamma))
    print("Key is: "+str(key))
    print("Decripting ciphertext with guessed key")
    print(shift_decrypt(ciphertext,key[1]))
