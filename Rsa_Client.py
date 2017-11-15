import time
import socket
host = 'localhost'
port = 13003                                            #Declaring port numbers
cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p = 61
q = 53
n = p*q
n = str(n)
i = 0
j = 4
cs.sendto(n, (host,port))                                #sending the value of n
n = int(n)                                              #converting n into int

while 1:
    try:
            
        message = raw_input('Enter: ')                  #dynamically entering data
        data = ''
        for m in message: #for loop
            message = (ord(m) ** 7) % n                 #message encryption
            data = data+str (message).zfill(4)           #Concatenating and padding 
        print 'Sending Ciphertext:', data    
        cs.sendto(data, (host, port))                   #Sending the cipher text
        cs.settimeout(30)                               #Timer started 
    except socket.timeout:                              #if timeout
        print "Timeout" 
        break                                           #disconnect
    try:
        modmessage, serverAddress = cs.recvfrom(2048) #receive from the server
        print 'Received Ciphertext', modmessage
        w = ''
        a = len(modmessage)/4                           #calculate the length of the received ciphertext
        for k in range(0,a):                            #for loop executes untill k is in range 0 to length
            z = modmessage[i:j]                         #parsing the digits
            
            y = pow(int(z), 1783)                       #raising to the power of d
            y = y % n                                   #result of mod n
            
            w = w + chr(y)                              #converting back to ASCII
            
            i = i+4
            j = j+4
        i = 0
        j = 4
        print 'decrypted Text:', w
        cs.settimeout(30)                               #timer start
    except socket.timeout:                              #if timeout  
        print "Timeout"
        break                                           #disconnect the connection
cs.close()                                              #close socket
