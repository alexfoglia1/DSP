import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 8080
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def sendReceive(msg):
    sock.sendto(msg, (UDP_IP, UDP_PORT))
    print(sock.recvfrom(1024)[0])

def Receive():
    print(sock.recvfrom(2048)[0])

sendReceive("STDLOAD#END")
Receive()
sendReceive("ENCODE#END")
sendReceive("umyu")
Receive()
sendReceive("QUIT#END")
    



