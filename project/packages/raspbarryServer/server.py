# pylint: disable-all
import project.packages.env as env
import socket
import json
import time


class ServerRaspy:

    HOST = env.currentEnv['serverHostRaspy']
    HOSTNTB = env.currentEnv['serverHostNtk']
    PORT = env.currentEnv['serverPort']

    def __init__(self):
        self.createCliente()

    def createCliente(self):
        self.socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketInstance.bind((self.HOST, self.PORT))
        self.socketInstance.listen(10)

    def sendMensage(self, mensage: str, type):
        try:
            print(mensage)
            jsonData = json.dumps({"mensage": mensage, "type": type})
            mensageJson = '{jsonData};'.format(jsonData=jsonData)
            self.socketInstance.sendto(str.encode(
                mensageJson), (self.HOSTNTB, self.PORT))
        except:
            time.sleep(5)
            self.sendMensage(mensage, type)
            pass


serverInstance = ServerRaspy()
