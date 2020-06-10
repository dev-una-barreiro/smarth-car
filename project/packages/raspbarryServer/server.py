import socket
import json


class ServerRaspy:

    HOST = 'localhost'
    PORT = 4444
    socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.createCliente()

    def createCliente(self):
        self.socketInstance.connect((self.HOST, self.PORT))

    def sendMensage(self, mensage: str, type):

        mensageJson = f'{json.dumps({"mensage": mensage, "type": type})};'
        self.socketInstance.send(mensageJson.encode())
        # while True:
        #     client, addr = self.socketInstance.accept()
        #     data = client.recv(1024)
        #     if data:
        #         print(data)
        #         break


serverInstance = ServerRaspy()

