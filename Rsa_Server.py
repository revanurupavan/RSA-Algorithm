import socket
host = 'localhost'                              #defining host
port = 13003                                    #port number
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ss.bind((host, port)) #binding the client and server
print " Bind Successful: Server ready"


i = 0
j = 4
n, clientAddress = ss.recvfrom(2048) #receive the value of n
n = int (n)
print "n =", n

while 1:
    try:
        w = ''
        message, clientAddress = ss.recvfrom(2048)  #receive the ciphertext
        print 'Received Ciphertext:', message
        a = len(message)/4 #calculate the lengt hof cipher text
        for k in range(0,a):    #for loop: k in range of 0 to a
            z = message[i:j]        #parsing the digits
            
            y = pow(int(z), 1783) % n           #z raised to the power of d
            
            
            w = w + chr(y)                      #converted to ascii and concatenated 
            
            i = i+4
            j = j+4
        print 'Decrypted Text:', w                  #print decrypted text
        i = 0
        j = 4
        modmessage = raw_input('Enter: ')           #enter the input to be  sent
        data = ''
        for m in modmessage:
            modmessage = (ord(m) ** 7) % n          #encrypting each character 
            data = data+str (modmessage).zfill(4)   #padding and concatenating
        print 'Sending Ciphertext', data
        ss.settimeout(30)       #timer start
    except socket.timeout:  #if timeout
        print "timeout"
        break                           #terminate the connection
    try:
        ss.sendto(data, clientAddress)    #send the data to the client
        ss.settimeout(30)               #timer start
        
    except socket.timeout:              #if timeout 
        print "timeout"
        break                           #connection terminates

ss.close()                              #socket closed
