from socket import *
from threading import Thread


def receive():
    while True:
        msg = client_socket.recv(BUFSIZ).decode("utf8")
        if msg == "{quit}":
            client_socket.close()
            break
        if not msg:
            break
        print(msg)


def send():
    while True:
        msg = input()
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            break


HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 39000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)
print(ADDR)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
send_thread = Thread(target=send)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()

#sudo kill $(sudo lsof -t -i:9001) (or)
#sudo kill `sudo lsof -t -i:9001`

