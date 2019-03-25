gamma = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def clean(txt):
    cln = txt.lower()
    for ch in txt:
        if ch not in gamma:
            cln = cln.replace(ch,"")
    return cln

def indexof(aset, anelem):
    for i in range(0,len(aset)):
        if aset[i] == anelem:
            return i
    return -1
