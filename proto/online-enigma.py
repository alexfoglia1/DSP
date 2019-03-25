from enigma import *
from threading import *
from socket import *

class ClientHandler:

    def __init__(self, client):
        self.client = client
        
    def run(self):
        while True:
            (command,(self.udp_ip,self.udp_port)) = self.client.recvfrom(1024)
            print "Received: "+str(command)
            print "From: "+str(self.udp_ip)+":"+str(self.udp_port)
            if not "#END" in command:
                self.__handleError__("MISSING #END")
            else:
                self.client.sendto("OK COMMAND#END",(self.udp_ip,self.udp_port))
                command = command[0:command.index("#END")]
                next = self.__handle__(command)
                if not next:
                    break
    def __handle__(self,command):
        command = command.upper()
        if command == "REFTABLE":
            self.__reftable__()
            return True
        elif command == "STDLOAD":
            self.__stdload__()
            return True
        elif command == "PRINT":
            self.__print__()
            return True
        elif command == "PLUGBOARD":
            self.__plugboard__()
            return True
        elif command == "BUILD":
            self.__build__()
            return True
        elif command == "ENCODE":
            self.__encode__()
            return True
        elif command == "QUIT":
            self.client.sendto("OK QUIT#END",(self.udp_ip,self.udp_port))
            return False
        else:
            self.__handleError__("UNEXISTING COMMAND")
            return True
    def __print__(self):
        try:
            self.client.sendto(self.enigma.toString()+"\r\n#END",(self.udp_ip,self.udp_port))
        except:
            self.__handleError__("CANNOT PRINT MACHINE DATA")
    def __stdload__(self):
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
        self.plugboard = steckered
        self.reftable = refTable
        self.enigma = Enigma(steckered,refTable,rotorsInit)
        self.client.sendto("OK STDLOAD#END",(self.udp_ip,self.udp_port))
    
    def __reftable__(self):
        try:
            command = self.client.recvfrom(2048)
            command = command.split(";")
            self.reftable = {}
            for pair in command:
                self.reftable[pair[0]]=pair[1]
            self.client.sendto("OK REFTABLE#END",(self.udp_ip,self.udp_port))
        except:
            self.__handleError__("WRONG REFLECTOR TABLE")

    def __plugboard__(self):
        try:
            command = self.client.recvfrom(2048)
            command = command.split(";")
            self.plugboard = {}
            if len(command) != 10:
                raise Exception()
            for pair in command:
                self.plugboard[pair[0]]=pair[1]
                self.plugboard[pair[1]]=pair[0]
            self.client.sendto("OK PLUGBOARD#END",(self.udp_ip,self.udp_port))
        except:
            self.__handleError__("WRONG PLUGBOARD")
    
    def __build__(self):
        try:
            rotorstate = int(self.client.recvfrom(1024))
            self.enigma = Enigma(self.plugboard,self.reftable,rotorstate)
            self.client.sendto("OK BUILD#END",(self.udp_ip,self.udp_port))
        except:
            self.__handleError__("CANNOT BUILD")
    
    def __encode__(self):
        try:
            string = self.client.recvfrom(4096)[0]
            encoded = self.enigma.encodeString(string)
            self.client.sendto("OK ENCODE "+string+"#END",(self.udp_ip,self.udp_port))
            self.client.sendto(encoded+"#END",(self.udp_ip,self.udp_port))
        except:
            self.__handleError__("CANNOT ENCODE")  

    def __handleError__(self, message):
        self.client.sendto(message+"#END",(self.udp_ip,self.udp_port))

class Server:
    
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((self.addr,self.port))
    def runInstance(self):
        client = ClientHandler(self.sock)
        t = Thread(target = client.run, args = ())
        t.start()

if __name__ == '__main__':
    s = Server("127.0.0.1",8080)
    s.runInstance()
    print "Server is listening . . ."

  
            
            
