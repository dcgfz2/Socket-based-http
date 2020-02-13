from socket import *
import sys

Host=sys.argv[1]
Port=sys.argv[2]
FileName=sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((Host,int(Port)))

Request = 'GET /'+ str(FileName) + ' HTTP/1.1\r\n'
clientSocket.send(Request.encode())

#Wait for reponse from server
message = ''

while True:
    ConvertBytes = ''
    ConvertBytes = clientSocket.recv(1024)
    message += ConvertBytes.decode()
    if ConvertBytes.decode() == '':
        break


print(message)

clientSocket.close()
