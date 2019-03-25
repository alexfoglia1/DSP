from VigenereEncrypter import *
from ShiftAttack import *
import sys

def create_matrix(text,m):
    matrix = []
    for i in range(0,len(text),m):
        row = ''.join(text[i:i+m])
        matrix.append(row)
    return matrix


def crack_vigenere(text,m):
    mat = create_matrix(text,m)
    key = []
    for i in range(0,m):
        Vi = create_freq_vector(create_vector(mat,i),gamma)
        key.append(crackShift(Vi,gamma))
    return key


if __name__ == '__main__':
    if len(sys.argv) == 1:
        text =  "kbrvdlikdihpbxhzenugntvnrfydttvvuihviwikvltgvmgfdgrtkbecfhgjmzvvrnpqthvujwegmgeyfofgebjvtlvvqveccsrzifmevxnuggxyvnvewmxvijrnbmsnvfnplbrrgyagbkekzhtupkmccpbkkxhvtfntmwmklhskbmsftwhrgttcrwrkvaiisugjzhsdkbrukkivenugvwmjgfnamwlvivnvpksfduafxbgbvxhrokewwcgkwglvivnvpksfdqnntmsfkbruifiwrgvnqtvjtlnytmlzjnvomkirucaitxeefprtbaisfqycvwxyvhgcsxeuzprcteswpihczxhvrxvcutpzmy"
        m = 8
    else:
        text = encrypt(sys.argv[1],sys.argv[2])
        m = len(sys.argv[2])
    print "Ciphertext is: "+text
    key = crack_vigenere(text,m)
    print key
    k = ''
    for triple in key:
        k = k + triple[2]
    print "Key is: "+k
    print "Plaintext:\n"+decrypt(text,k)
    
    
    
