import math

gamma = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
english_freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]

def clean(text):
    newstr = text.lower()
    for ch in newstr:
        if ch not in gamma:
            newstr = newstr.replace(ch,'')
    return newstr
    
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

def all_qgrams(q, text):
    qgrams = []
    i = 0
    while i < len(text):
        next_qgram = text[i:i+q]
        if not next_qgram in qgrams:
            qgrams.append(next_qgram)
        i = i + q
    return qgrams

def qgram_count(qgrams, text):
    q = len(qgrams[0])
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

def plot_dictionary(q,d,title):
    import matplotlib.pyplot as plt
    keys = list(d.keys())
    keys.sort()
    values = []
    for key in keys:
        values.append(d[key])
    plt.bar(keys,values,color = 'b')
    plt.title(str(q)+title)
    plt.show()

def exit_with_prompt(prompt):
    print(prompt)
    exit()

def shannon_h(qgrams):
    h_dict = dict()
    for A in qgrams:
        h = 0
        for a in A:
            fa = float(fi(a,A))
            h = h + (fa/float(len(A)))*math.log2(fa/float(len(A)))
        h_dict[str(A)] = -h
    print(h_dict)
    return h_dict

if __name__ == '__main__':
    import sys
    txt = ""
    try:
        txt = ''.join(open(sys.argv[1],'r+').readlines())
        txt = clean(txt)
    except:
        exit_with_prompt("No text provided as argument, exiting . . .")
    print("Read string: "+txt+"\n")
    print("C index = " + str(c_index(txt)))
    try:
        q = int(input("Insert max m\n"))
    except:
        exit_with_prompt("Not a valid integer, exiting . . .")
    if q>0:
        for i in range(1,q+1):
            qgrams = all_qgrams(i, txt)
            for qgram in qgrams:
                if len(qgram)>1:
                    print("c index of "+qgram+" = "+str(c_index(qgram)))
            #plot_dictionary(i,shannon_h(qgrams),"-gram H distribution")
            #count = qgram_count(qgrams, txt)
             #plot_dictionary(i,count,"-gram frequencies")

