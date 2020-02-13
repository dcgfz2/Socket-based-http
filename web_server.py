from socket import *
import threading
import sys

def serve(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        print('SENT DATA:')
        print(outputdata)

        #Send HTTP header line through socket
        HTTPSTATUS='HTTP/1.1 200 OK \r\n'
        print('STATUS: '+ HTTPSTATUS)
        connectionSocket.send(HTTPSTATUS.encode('utf-8'))

        #Send requested file to client
            
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
            
        connectionSocket.close()
        
    except IOError:
        #Response when file isn't found 
        HTTPSTATUS="HTTP/1.1 404 Not Found\r\n\r\n"
        print('STATUS: '+ HTTPSTATUS)
        File404="<html><head></head><body><h1>404 FILE NOT IN THIS SERVER :^)</h1></body></html>\r\n"
        connectionSocket.send(HTTPSTATUS.encode())
        connectionSocket.send(File404.encode())
        
        #Closing client socket
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)

#PREPARE SOCKET

Port = 1400

serverSocket.bind(("",Port))

#listen to port 1400 to check for connection request
serverSocket.listen(10)

threadList = []

while True:
    #Get connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    print(addr)
    serveThread = threading.Thread(target=serve, args=(connectionSocket, addr))
    serveThread.start()
    threadList.append(serveThread)
    print(threadList)

    

serverSocket.close()

sys.exit()
