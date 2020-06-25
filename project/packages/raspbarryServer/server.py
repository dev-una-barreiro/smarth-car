# pylint: disable-all
import project.packages.env as env
import socket
import json
import time


class ServerRaspy:

    HOST = env.currentEnv['serverHostNtk']
    PORT = env.currentEnv['serverPort']
    socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.createCliente()

    def createCliente(self):
        self.socketInstance.connect((self.HOST, self.PORT))

    def sendMensage(self, mensage: str, type):
        try:
            print(mensage)
            jsonData = json.dumps({"mensage": mensage, "type": type})
            mensageJson = '{jsonData};'.format(jsonData=jsonData)
            self.socketInstance.sendall(str.encode(mensageJson))
        except:
            time.sleep(5)
            self.sendMensage(mensage, type)
            pass
