def clean(text):
	newstr = text.lower()
	newstr = newstr.replace(" ","")
	newstr = newstr.replace(".","")
	newstr = newstr.replace("?","")
	newstr = newstr.replace("!","")
	return newstr

def all_qgrams(q, text):
	qgrams = []
	i = 0
	while i < len(text):
		qgrams.append(text[i:i+q])
		i = i + q
	return qgrams

def qgram_count(q, text):
	text = clean(text)
	qgrams = all_qgrams(q, text)
	count = dict()
	for qgram in qgrams:
		i = 0
		n = 0
		while i < len(text):
			if text[i:i+q] == qgram:
				n = n + 1
			i = i + q
		count[qgram] = n
	return count

def plot_dictionary(q,d):
	import matplotlib.pyplot as plt
	plt.bar(list(d.keys()),d.values(),color = 'b')
	plt.title(str(q)+"-gram frequencies")
	plt.show()

def exit_with_prompt(prompt):
	print(prompt)
	exit()

def parse(argv):
	txt = argv[1]
	i = 2
	while i<len(argv):
		txt = txt + argv[i]
		i = i + 1
	return txt

if __name__ == '__main__':
	import sys
	txt = ""
	try:
		txt = parse(sys.argv)
	except:
		exit_with_prompt("No text provided as argument, exiting . . .")
	print("Read string: "+txt+"\n")
	try:
		q = int(input("Insert q\n"))
	except:
		exit_with_prompt("Not a valid integer, exiting . . .")
	count = qgram_count(q, txt)
	plot_dictionary(q,count)