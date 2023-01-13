# UDP Pinger Client

from datetime import datetime 
from socket import * 
from time import time


def main():
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET , SOCK_DGRAM)
    message = 'Ping'
    counter = 10
    i=0
    
    print ('Now attempting', counter, 'pings are being tried.\n')
    while i < counter:
        i+=1
        print ('\n Ping attempt number:', i, 'is currently in progress.\n ')
        print ('There are', counter-i ,'attempts left.\n')
        dt = datetime.now()

        clientSocket.sendto(b'Ping',(serverName,serverPort))
        
        clientSocket.settimeout(1)
        
        try:
            modifiedMessage,serverAddress= clientSocket.recvfrom(1024)
            dt2 = datetime.now()
            et = dt - dt2;
            print (modifiedMessage)
            print ('Time elapsed: ', et.microseconds, 'microseconds\n')
        except timeout:
            print('Request timed out. Your connection has timed out! Please try again')
    
    if i==10:

        print ('Socket has been closed! No more pings!')   
    
    clientSocket.close()
    
    pass
if __name__ == '__main__':
    main()