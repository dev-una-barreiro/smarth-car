# pylint: disable-all
import project.packages.env as env
import socket
import json
import time


class ServerRaspy:

    HOST = env.currentEnv['serverHostNtk']
    PORT = env.currentEnv['serverPort']

    def __init__(self):
        self.createCliente()

    def createCliente(self):
        self.socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketInstance.bind((HOST, PORT))
        self.socketInstance.listen(10)
        while True:
            client, addr = socketClient.accept()
            data = client.recv(1024)
            if data:
                print('Received', repr(data.decode('utf-8')))
            else:
                print('await')

    def sendMensage(self, mensage: str, type):
        try:
            print(mensage)
            jsonData = json.dumps({"mensage": mensage, "type": type})
            mensageJson = '{jsonData};'.format(jsonData=jsonData)
            self.socketInstance.send(str.encode(mensageJson))
        except:
            time.sleep(5)
            self.sendMensage(mensage, type)
            pass


serverInstance = ServerRaspy()
