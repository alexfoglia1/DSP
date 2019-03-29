#This is the code of Exercise 3.1
#It needs libraries scipy, numpy and matplotlib, both available with pip: launch pip install (library name) if any is missing
#In order to execute the code, user has to launch python3 mgram.py [pathToFile] where [pathToFile] is the path of the file containing the text to be analyzed [e.g mobydick.txt]
#
#Author: Alex Foglia, 6336805

import math                                                         #Library used to compute logarithm
from scipy import stats                                             #Libraries used to print a distribution overview
import numpy as np

gamma = ['a','b','c','d','e','f','g','h','i','j','k','l',\
        'm','n','o','p','m','r','s','t','u','v','w','x','y','z']    #Defined alphabet a priori   
                                        
english_freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,\
        6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,\
        0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]#English letter frequency vector

def clean(text):                                                    #Routine used to clean the text as specified
    newstr = text.lower()                                           #Convert string to lowercase
    for ch in newstr:                                               #Foreach character in the text, if it is not included in gamma, replace it
        if ch not in gamma:
            newstr = newstr.replace(ch,'')
    return newstr                                                   #Returning clean text to caller
    
def fi(string,text):                                                #Routine used to count the occurences of a given string in a given text
    c = 0
    for i in range(0,len(text)):
        if text[i] == string:
            c = c + 1
    return c


def all_mgrams(m, text):                                            #Routine used to compute all m grams in a given text
    mgrams = []
    i = 0
    while i < len(text):
        next_mgram = text[i:i+m]                                    #Substring of interest
        if next_mgram not in mgrams:
            mgrams.append(next_mgram)
        i = i + m
    return mgrams                                                   #Returning all m grams to caller

def mgram_count(mgrams, text):                                      #Routine used to count all mgram occurences in a given text
    m = len(mgrams[0])                                              #Compute m
    count = dict()                                                  #Dictionary initialization
    size = len(text)
    for mgram in mgrams:                                            #Foreach mgram count its frequency and assign it to dictionary[mgram]
        _text = text.replace(mgram,"")
        delta = size - len(_text)
        count[mgram] = delta/m                                           
    return count                                                    #Returning dictionary to caller

def plot_dictionary(d,title="Letter frequency in provided text"):   #Routine used to plot a dictionary representing a distribution as histogram
    import matplotlib.pyplot as plt                                 #Import matplotlib.pyplot library in order to being able to plot a dictionary
    keys = list(d.keys())                                           #Rearrange keys in alphabetical order
    keys.sort()
    values = []
    for key in keys:                                                #Ordering the distribution
        values.append(d[key])
    plt.bar(keys,values,color = 'b')                                #Construct and show histogram
    plt.title(title)
    plt.show()

def __readFile__():                                                 #Routine used to read the input file provided as argument
    import sys                                                      #Import of sys module in order to being able to parse CLI arguments
    try:
        txt = ''.join(open(sys.argv[1],'r+').readlines())           #Constructing the string reading all lines in provided file
        txt = clean(txt)                                            #Cleaning text as requested
        return txt                                                  #Returning read text to caller
    except:
        raise Exception("No valid file provided as argument")       #If something went wrong, raise an Exception

def __hist__(txt):                                                  #Routine used to plot histogram of each letter frequency
    d = {}                                                          #Dictionary initialization
    for letter in gamma:                                            #Foreach letter in the alphabet
        d[letter] = float(fi(letter,txt))/len(txt)                  #d[letter] is the frequency of each letter in the text divided by the length of the text
    plot_dictionary(d)                                              #Plot of the histogram and print distribution

def entropy_dic(d):                                                 #Routine used to calculate Shannon Entropy of a given dictionary of a mgram frequency distribution
    n = sum(d.values())                                             #Applying formula
    entropy = 0     
    for key in d.keys():
        entropy += d[key] / n * math.log2(d[key] / n)
    return (-1) * (entropy) / math.log2(len(d.keys()))

def c_index(d):                                                     #Routine used to calculate coincide index of a given dictionary of a mgram frequency distribution
    cIndex = 0.0                                                    #Applying formula
    n = float(sum(d.values()))                      
    for key in d.keys():
        cIndex += float(d[key])*float(d[key]-1)
    return cIndex / ((n)*n-1)

def __distribSummary__(m, d):                                       #Routine used to print a summary of the distribution of mgrams
    d = stats.describe(np.array(list(d.values())))
    print("{}".format(d).replace("DescribeResult","Distribution of {}-grams summary: ".format(m)))

#-----------------------START DRIVER CODE---------------------------#
if __name__ == '__main__':                                              #Check if the script is called directly
    txt = __readFile__()                                                #Reading input file (e.g. mobydick.txt)
    __hist__(txt)                                                       #Plot histogram of relative letter frequencies in parsed text
    m = 4                                                               #Maximum m
    for j in range(1,m+1):                                              #For mgrams with m from 1 to 4                                            
        mgrams = all_mgrams(j, txt)                                     #Get all m grams
        c = mgram_count(mgrams, txt)                                    #Count all absolute mgrams frequencies distribution
        cr = {}                                                         #Construct relative mgrams frequencies distribution
        for key in c.keys():
            cr[key] = float(c[key])/(float(len(txt))/j)
        __distribSummary__(j,cr)
        cIndex = c_index(c)                                             #Compute and print coincidence index of mgram distribution
        print("C-index of {}-grams distribution = {}".format(j,cIndex))
        h = entropy_dic(c)                                              #Compute and print entropy of mgram distribution
        print("Entropy of {}-grams distribution = {}".format(j,h))
#-----------------------END DRIVER CODE-----------------------------#

