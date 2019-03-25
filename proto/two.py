cipher = [ord('H'),ord('R'),ord('O'),ord('F'),ord('S'),ord('X')]
target = [ord('R'),ord('E'),ord('S'),ord('I'),ord('S'),ord('T')]
_target= [ord('G'),ord('I'),ord('V'),ord('E'),ord('U'),ord('P')]
key    = [0,0,0,0,0,0]
_key   = [0,0,0,0,0,0]

def xor(t,k):
	return t^k

def totext(list_of_int):
	list_of_char = list(list_of_int)
	for i in range(0,len(list_of_int)):
		list_of_char[i] = chr(list_of_int[i])
	return list_of_char

for i in range(0,len(key)):
	key[i]  = xor(cipher[i], target[i])
	_key[i] = xor(cipher[i],_target[i])
	
actual =  []
_actua = []
print("CIPHERTEXT:\t"+str(totext(cipher))+"\n")
for i in range(0,len(key)):
	actual.append(xor(cipher[i], key[i]))
	_actua.append(xor(cipher[i],_key[i]))
print("KEY 1 :\t\t"+str(key)  +"\nPLAINTEXT 1:\t" + str(totext(actual))+"\n")
print("KEY 2 :\t\t"+str(_key) +"\nPLAINTEXT 2:\t" + str(totext(_actua)))