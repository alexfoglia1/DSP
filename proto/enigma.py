from gamma import *

class Rotor:
    def __init__(self, state, ref):
        self.state=state
        self.r = ref
    def encode(self, letter, inverse):
        index = indexof(gamma, letter)
        if not inverse:
            fIndex = index + self.state
            self.state = (self.state + 1)
            return gamma[fIndex%len(gamma)]
        else:
            fInvIndex = index - self.state
            return gamma[fInvIndex%len(gamma)]
    def getState(self):
        return self.state

class Reflector:
    def __init__(self, table):
        self.table = table
    def encode(self, letter):
        return self.table[letter]
    def toString(self):
        return str(self.table)

class Plugboard:
    def __init__(self, steck):
        self.steck = steck
    def encode(self, letter):
        if letter in self.steck.keys():
            letter = self.steck[letter]
        return letter
    def toString(self):
        return str(self.steck)

class Enigma:
    def __init__(self, steckered, reflectorTable, rotorsInit):
        self.plugboard = Plugboard(steckered)
        self.reflector = Reflector(reflectorTable)
        self.r1 = Rotor(rotorsInit,self.reflector)

    def __encode__(self, letter):
        print ("Letter in: "+letter)
        plugOut = self.plugboard.encode(letter)
        print ("Plugboard out: "+plugOut)
        r1Out = self.r1.encode(plugOut,False)
        print ("Rotor 1 output: "+r1Out)
        reflected = self.reflector.encode(r1Out)
        print ("Reflected output: "+reflected)
        r1Out = self.r1.encode(reflected,True)
        print ("Inverse rotor 1 output: "+r1Out)
        plugOut = self.plugboard.encode(r1Out)
        print ("Plugboard out: "+plugOut)
        return plugOut
    def toString(self):
        return "ENIGMA MACHINE\r\n[Plugboard: "+self.plugboard.toString()+"]\r\n[Rotor state: "+str(self.r1.getState())+"]\r\n[Reflector: "+self.reflector.toString()+"]"
    def encodeString(self, string):
        chars = []
        string = clean(string)
        for ch in string:
            if ch != "":
                chars.append(self.__encode__(ch))
        return ''.join(chars)

if __name__ == '__main__':
    refTable = {}
    refTable['a']='z'
    refTable['b']='y'
    refTable['c']='x'
    refTable['d']='w'
    refTable['e']='v'
    refTable['f']='u'
    refTable['g']='t'
    refTable['h']='s'
    refTable['i']='r'
    refTable['j']='q'
    refTable['k']='p'
    refTable['l']='o'
    refTable['m']='n'
    refTable['n']='m'
    refTable['o']='l'
    refTable['p']='k'
    refTable['q']='j'
    refTable['r']='i'
    refTable['s']='h'
    refTable['t']='g'
    refTable['u']='f'
    refTable['v']='e'
    refTable['w']='d'
    refTable['x']='c'
    refTable['y']='b'
    refTable['z']='a'
    steckered = {}
    steckered['q'] = 'p'
    steckered['a'] = 'v'
    steckered['z'] = 't'
    steckered['w'] = 'g'
    steckered['s'] = 'b'
    steckered['x'] = 'y'
    steckered['e'] = 'h'
    steckered['d'] = 'n'
    steckered['c'] = 'u'
    steckered['r'] = 'j'
    steckered['p'] = 'q'
    steckered['v'] = 'a'
    steckered['t'] = 'z'
    steckered['g'] = 'w'
    steckered['b'] = 's'
    steckered['y'] = 'x'
    steckered['h'] = 'e'
    steckered['n'] = 'd'
    steckered['u'] = 'c'
    steckered['j'] = 'r'
    rotorsInit = 1
    en = Enigma(steckered,refTable,rotorsInit)
    en2 = Enigma(steckered,refTable,rotorsInit)
    encoded = en.encodeString("messaggio segreto")
    decoded = en2.encodeString(encoded)
    print(encoded)
    print(decoded)
    
