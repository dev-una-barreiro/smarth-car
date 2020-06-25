# pylint: disable-all
import project.packages.raspbarryServer.server
import project.packages.env as env
import socket
import json


class ServerRaspy:

    HOST = env.currentEnv['serverHostRaspy']
    PORT = env.currentEnv['serverPort']
    socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.createCliente()

    def createCliente(self):
        self.socketInstance.connect((self.HOST, self.PORT))

    def sendMensage(self, mensage: str, type):
        jsonData = json.dumps({"mensage": mensage, "type": type})
        mensageJson = '{jsonData};'.format(jsonData=jsonData)
        self.socketInstance.send(mensageJson.encode())


serverInstance = ServerRaspy()
