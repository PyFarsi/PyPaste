import socket
import secrets
from paster import paste
def server():
    # create the socket
    # AF_INET => IPv4
    # SOCK_STREAM => TCP Connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('0.0.0.0', 9999))

    s.listen(10)

    while True:
        try:
            clientSocket, address = s.accept()
            print(f"Connection from {address} has been established")
            

            full_message = ""
            while True:
                data = clientSocket.recv(32768)
                if len(data) <= 0:

                    break
                full_message += data.decode('utf-8')

            res = paste(full_message)
            
            clientSocket.sendall(
                bytes('127.0.0.1:5000/'+res+"\n", "utf-8"))
            clientSocket.shutdown(socket.SHUT_WR)
        except:
            pass
server()