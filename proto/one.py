from zero import *
gamma = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def fi(letter,text):
	c = 0
	for i in range(0,len(text)):
		if text[i] == letter:
			c = c + 1
	return c

def c_index(text):
	index = .0
	text = clean(text)
	n = len(text)
	for f in gamma:
		_fi = fi(f,text)
		ratio = (_fi*(_fi - 1))/(n*(n-1))
		index = index + ratio
	return index

if __name__ == "__main__":
	import sys
	txt = ""
	try:
		txt = parse(sys.argv)
	except:
		exit_with_prompt("No text provided as argument, exiting . . .")
	print("C index of "+txt+" = " + str(c_index(txt)))
	